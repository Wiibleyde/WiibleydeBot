from service.config import ConfigService
from service.logger import LoggerService
from service.twitch import TwitchService
from service.youtube import YoutubeService
from service.varSave import VarSaveService

import discord
from discord import app_commands
from discord.ext import commands, tasks
import argparse

def readArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config',help='config file name')
    parser.add_argument('-d', '--debug', action='store_true', help='debug mode')    
    args = parser.parse_args()
    return args

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    loggerService.log('Bot is ready')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Starting..."))
    try:
        synced = await bot.tree.sync()
        loggerService.debug(f"Synced {len(synced)} commands")
        loggerService.debug(f"Commands: {synced}")
        isOnLive.start()
    except Exception as e:
        loggerService.error(f"Failed to sync commands: {e}")
    
@bot.tree.command(name='live',description='Savoir si Wiibleyde est en live')
async def live(interaction: discord.Interaction):
    twitchService = TwitchService()
    if twitchService.checkIfUserIsStreaming():
        embed = discord.Embed(title="Wiibleyde est en live !")
        embed.add_field(name="Lien",value=f"https://www.twitch.tv/{configService.getTwitchChannel()}")
        embed.add_field(name="Titre",value=twitchService.getStreamTitle())
        embed.add_field(name="Jeu",value=twitchService.getStreamGame())
        embed.add_field(name="Viewers",value=twitchService.getStreamViewers())
        embed.set_thumbnail(url=twitchService.getStreamThumbnail())
        embed.set_image(url=twitchService.getStreamPreview())
        embed.set_footer(text="Wiibleyde est en live !")
        await interaction.response.send_message(embed=embed,ephemeral=True)
    else:
        await interaction.response.send_message("Wiibleyde n'est pas en live",ephemeral=True)

@tasks.loop(seconds=10)
async def isOnLive():
    twitchService = TwitchService()
    if twitchService.isChannelLive():
        if varSaver.getVar('liveSend'):
            # get the only one message of the channel and modify it to update the title and other things
            # the message should be the last of the channel
            # await bot.get_channel(configService.getTwitchTextChannelId()).fetch_message()
            return
        varSaver.saveVar('liveSend',True)
        embed = discord.Embed(title="Wiibleyde est en live !")
        embed.add_field(name="Lien",value=f"https://www.twitch.tv/{configService.getTwitchChannel()}")
        embed.add_field(name="Titre",value=twitchService.getStreamTitle())
        embed.add_field(name="Jeu",value=twitchService.getStreamGame())
        embed.add_field(name="Viewers",value=twitchService.getStreamViewers())
        embed.set_thumbnail(url=twitchService.getStreamThumbnail())
        embed.set_image(url=twitchService.getStreamPreview())
        embed.set_footer(text="Wiibleyde est en live !")
        await bot.get_channel(configService.getTwitchTextChannelId()).send(embed=embed)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Wiibleyde online !"))
    else:
        if not varSaver.getVar('liveSend'):
            return
        varSaver.saveVar('liveSend',False)
        await bot.get_channel(configService.getTwitchTextChannelId()).purge()
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="pas Wiibleyde"))

@bot.tree.command(name='youtube',description='Dernière vidéo posté sur la chaîne de Wiibleyde')
async def youtube(interaction: discord.Interaction):
    youtubeService = YoutubeService(configService.getYoutubeApiKey(),configService.getYoutubeChannel())
    if youtubeService.hasChannelNewVideo():
        embed = discord.Embed(title="Nouvelle vidéo !")
        embed.add_field(name="Lien",value=youtubeService.getChannelNewVideoUrl())
        embed.add_field(name="Titre",value=youtubeService.getChannelNewVideoTitle())
        embed.add_field(name="Description",value=f"{youtubeService.getChannelNewVideoDescription()[0:100]}...")
        embed.set_image(url=youtubeService.getChannelNewVideoThumbnail())
        embed.set_footer(text="Nouvelle vidéo !")
        await interaction.response.send_message(embed=embed,ephemeral=True)
    else:
        await interaction.response.send_message("Aucune nouvelle vidéo",ephemeral=True)

@tasks.loop(seconds=10)
async def hasNewYoutubeVideo():
    youtubeService = YoutubeService()
    if youtubeService.hasChannelNewVideo():
        if varSaver.getVar('youtubeSend'):
            return
        varSaver.saveVar('youtubeSend',True)
        embed = discord.Embed(title="Nouvelle vidéo !")
        embed.add_field(name="Lien",value=youtubeService.getChannelNewVideoUrl())
        embed.add_field(name="Titre",value=youtubeService.getChannelNewVideoTitle())
        embed.add_field(name="Description",value=f"{youtubeService.getChannelNewVideoDescription()[0:10]}...")
        embed.set_image(url=youtubeService.getChannelNewVideoThumbnail())
        embed.set_footer(text="Nouvelle vidéo !")
        await bot.get_channel(configService.getYoutubeTextChannelId()).send(embed=embed)
    else:
        if not varSaver.getVar('youtubeSend'):
            return
        varSaver.saveVar('youtubeSend',False)

@bot.tree.command(name='set', description="[ADMIN] set config value")
@commands.has_permissions(administrator=True)
async def setConfig(interaction: discord.Interaction, key: str, value: str):
    oldValue = configService.getValue(key)
    configService.setValue(key,value)
    await interaction.response.send_message(f"Set {key} from {oldValue} to {value}",ephemeral=True)

if __name__ == '__main__':
    args = readArgs()
    varSaver = VarSaveService('var.json')
    loggerService = LoggerService('logs.log',args.debug)
    loggerService.log('Bot is starting')
    configService = ConfigService('config.yaml')
    botToken = configService.getBotToken()
    if botToken == 'your bot token':
        loggerService.warning("Bot token not set, the bot won't boot !")
        loggerService.log("Stopping program...")
        exit()
    bot.run(botToken)