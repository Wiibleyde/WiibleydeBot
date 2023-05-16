import yaml
import os

class ConfigService:
    def __init__(self,filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            self.createConfig()
        self.config = self.loadConfig()

    def createConfig(self):
        with open(self.filename,'w') as f:
            config = {
                'bot_token' : 'your bot token',
                'twitch_channel' : 'channel name',
                'youtube_channel' : 'channel name',
                'twitch_text_channel_id' : 'your twitch live alert',
                'youtube_text_channel_id' : 'your youtube live alert',
                'twitch_api_key' : 'your twitch api key',
                'twitch_client_id' : 'your twitch client id',
                'youtube_api_key' : 'your youtube api key'
            }
            yaml.dump(config,f)

    def loadConfig(self):
        with open(self.filename,'r') as f:
            return yaml.load(f,Loader=yaml.FullLoader)
        
    def getValue(self,key):
        return self.config[key]
        
    def getBotToken(self):
        return self.config['bot_token']
    
    def getTwitchChannel(self):
        return self.config['twitch_channel']
    
    def getYoutubeChannel(self):
        return self.config['youtube_channel']
    
    def getTwitchTextChannelId(self):
        return self.config['twitch_text_channel_id']
    
    def getYoutubeTextChannelId(self):
        return self.config['youtube_text_channel_id']
    
    def getTwitchApiKey(self):
        return self.config['twitch_api_key']
    
    def getTwitchClientId(self):
        return self.config['twitch_client_id']
    
    def getYoutubeApiKey(self):
        return self.config['youtube_api_key']
    
    def setValue(self,key,value):
        self.config[key] = value
        self.saveConfig()
    
    def setBotToken(self,token):
        self.config['bot_token'] = token
        self.saveConfig()

    def setTwitchChannel(self,channel):
        self.config['twitch_channel'] = channel
        self.saveConfig()

    def setYoutubeChannel(self,channel):
        self.config['youtube_channel'] = channel
        self.saveConfig()

    def setTwitchTextChannelId(self,channelId):
        self.config['twitch_text_channel_id'] = channelId
        self.saveConfig()

    def setYoutubeTextChannelId(self,channelId):
        self.config['youtube_text_channel_id'] = channelId
        self.saveConfig()

    def setTwitchApiKey(self,apiKey):
        self.config['twitch_api_key'] = apiKey
        self.saveConfig()

    def setTwitchClientId(self,clientId):
        self.config['twitch_client_id'] = clientId
        self.saveConfig()

    def setYoutubeApiKey(self,apiKey):
        self.config['youtube_api_key'] = apiKey
        self.saveConfig()

    def saveConfig(self):
        with open(self.filename,'w') as f:
            yaml.dump(self.config,f)

    

