from .config import ConfigService

import requests
import json

class TwitchService:
    def __init__(self):
        self.channelName = ConfigService('config.yaml').getTwitchApiKey()
        self.clientId = ConfigService('config.yaml').getTwitchClientId()
        self.apiKey = ConfigService('config.yaml').getTwitchApiKey()

    def getAccessToken(self):
        url = 'https://id.twitch.tv/oauth2/token'
        data = {
            'client_id': self.clientId,
            'client_secret': self.apiKey,
            'grant_type': 'client_credentials'
        }
        response = requests.post(url, data=data)

        if response.status_code == 200:
            json_data = response.json()
            return json_data['access_token']
        else:
            return False
    
    def checkIfUserIsStreaming(self):
        headers = {
            "Authorization": f"Bearer {self.getAccessToken()}",
            "Client-Id": self.clientId
        }
        twitch_api_stream_url = f"https://api.twitch.tv/helix/streams"
        response = requests.get(twitch_api_stream_url, headers=headers)
        print(response)

        if response.status_code == 200:
            json_data = response.json()
            if json_data["data"]:
                return True
            else:
                return False
        else:
            return False
        
    def getStreamInfo(self):
        headers = {
            "Authorization": f"Bearer {self.getAccessToken()}",
            "Client-ID": self.clientId
        }
        twitch_api_stream_url = f"https://api.twitch.tv/helix/streams"
        response = requests.get(twitch_api_stream_url, headers=headers)
        return response.json()['data'][0]
    
    def getStreamInfoFromId(self, streamId):
        headers = {
            "Authorization": f"Bearer {self.getAccessToken()}",
            "Client-ID": self.clientId
        }
        twitch_api_stream_url = f"https://api.twitch.tv/helix/streams"
        response = requests.get(twitch_api_stream_url, headers=headers)
        return response.json()['data'][0]
    
    def getStreamTitle(self):
        return self.getStreamInfo()['title']
    
    def getStreamViewers(self):
        return self.getStreamInfo()['viewer_count']
    
    def getStreamThumbnail(self):
        return self.getStreamInfo()['thumbnail_url']

    def getStreamPreview(self):
        return self.getStreamInfo()['thumbnail_url'].replace('{width}', '1920').replace('{height}', '1080')