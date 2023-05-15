from .config import ConfigService

import requests

class TwitchService:
    def __init__(self):
        self.channelName = ConfigService('config.yaml').getTwitchApiKey()
        self.apiKey = ConfigService('config.yaml').getTwitchApiKey()
    
    def isChannelLive(self):
        url = f'https://api.twitch.tv/helix/streams?user_login={self.channelName}'
        headers = {
            'Client-ID' : self.apiKey
        }
        response = requests.get(url,headers=headers).json()
        if len(response['data']) == 0:
            return False
        else:
            return True
        
    def getChannelId(self):
        url = f'https://api.twitch.tv/helix/users?login={self.channelName}'
        headers = {
            'Client-ID' : self.apiKey
        }
        response = requests.get(url,headers=headers).json()
        return response['data'][0]['id']
    
    def getChannelLiveInfo(self):
        url = f'https://api.twitch.tv/helix/streams?user_login={self.channelName}'
        headers = {
            'Client-ID' : self.apiKey
        }
        response = requests.get(url,headers=headers).json()
        return response['data'][0]
    
    def getChannelLiveTitle(self):
        return self.getChannelLiveInfo()['title']
    
    def getChannelLiveGame(self):
        return self.getChannelLiveInfo()['game_name']
    
    def getChannelLiveViewers(self):
        return self.getChannelLiveInfo()['viewer_count']
    
    def getChannelLiveThumbnail(self):
        return self.getChannelLiveInfo()['thumbnail_url']
    
    def getChannelLiveUrl(self):
        return f'https://www.twitch.tv/{self.channelName}'
    
    def getChannelLivePreview(self):
        return self.getChannelLiveThumbnail().replace('{width}','1920').replace('{height}','1080')
    
    def getChannelLiveThumbnail(self):
        return self.getChannelLiveThumbnail().replace('{width}','440').replace('{height}','248')
    
    def getChannelLiveStartedAt(self):
        return self.getChannelLiveInfo()['started_at']
    
    def getChannelLiveLanguage(self):
        return self.getChannelLiveInfo()['language']
    
    def getChannelLiveType(self):
        return self.getChannelLiveInfo()['type']
    
    def getChannelLiveDuration(self):
        return self.getChannelLiveInfo()['duration']
    
    def getChannelLiveId(self):
        return self.getChannelLiveInfo()['id']
    
    def getChannelLiveTagIds(self):
        return self.getChannelLiveInfo()['tag_ids']
    
    def getChannelLiveThumbnailUrl(self):
        return self.getChannelLiveInfo()['thumbnail_url']