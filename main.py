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
        if synced:
            loggerService.log('Slash commands synced')
        else:
            loggerService.log('Slash commands not synced')
    except Exception as e:
        loggerService.log(f'Error while syncing slash commands: {e}')
    isOnLive.start()
    
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

@bot.tree.command(name='set', description="[ADMIN] set config value")
@commands.has_permissions(administrator=True)
async def setConfig(interaction: discord.Interaction, key: str, value: str):
    try:
        oldValue = configService.getValue(key)
        configService.setValue(key,value)
        await interaction.response.send_message(f"Set {key} from {oldValue} to {value}",ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"Error while setting {key} to {value}: {e}",ephemeral=True)

@tasks.loop(seconds=10)
async def isOnLive():
    twitchService = TwitchService()
    if twitchService.checkIfUserIsStreaming():
        if varSaver.getVar('liveSend'):
            return
        varSaver.saveVar('liveSend',True)
        embed = discord.Embed(title="Wiibleyde est en live !")
        embed.add_field(name="Lien",value=f"https://www.twitch.tv/{configService.getTwitchChannel()}")
        embed.add_field(name="Titre",value=twitchService.getStreamTitle())
        embed.add_field(name="Jeu",value=twitchService.getStreamGameName())
        embed.add_field(name="Viewers",value=twitchService.getStreamViewers())
        embed.set_thumbnail(url=twitchService.getStreamThumbnail())
        embed.set_image(url=twitchService.getStreamPreview())
        embed.set_footer(text="Wiibleyde est en live !")
        await bot.get_channel(configService.getTwitchTextChannelId()).send(embed=embed)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Wiibleyde online !"))
    else:
        if not varSaver.getVar('liveSend'):
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="pas Wiibleyde"))
            return
        varSaver.saveVar('liveSend',False)
        await bot.get_channel(configService.getTwitchTextChannelId()).purge()
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="pas Wiibleyde"))

if __name__ == '__main__':
    args = readArgs()
    if args.debug:
        print("Debug mode enabled")
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