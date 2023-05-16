from .config import ConfigService

import requests
import json

class TwitchService:
    def __init__(self):
        self.channelName = ConfigService('config.yaml').getTwitchApiKey()
        self.clientId = ConfigService('config.yaml').getTwitchClientId()
    
    def checkIfUserIsStreaming(self):
        twitch_api_stream_url = "https://api.twitch.tv/kraken/streams/" + self.channelName + "?client_id=" + self.clientId
        response = requests.get(twitch_api_stream_url)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            if json_data['stream'] == None:
                return False
            else:
                return True
        else:
            return False
        
    def getStreamTitle(self):
        twitch_api_stream_url = "https://api.twitch.tv/kraken/streams/" + self.channelName + "?client_id=" + self.clientId
        response = requests.get(twitch_api_stream_url)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            return json_data['stream']['channel']['status']
        else:
            return None
        
    def getStreamGame(self):
        twitch_api_stream_url = "https://api.twitch.tv/kraken/streams/" + self.channelName + "?client_id=" + self.clientId
        response = requests.get(twitch_api_stream_url)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            return json_data['stream']['game']
        else:
            return None
        
    def getStreamViewers(self):
        twitch_api_stream_url = "https://api.twitch.tv/kraken/streams/" + self.channelName + "?client_id=" + self.clientId
        response = requests.get(twitch_api_stream_url)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            return json_data['stream']['viewers']
        else:
            return None
        
    def getStreamPreview(self):
        twitch_api_stream_url = "https://api.twitch.tv/kraken/streams/" + self.channelName + "?client_id=" + self.clientId
        response = requests.get(twitch_api_stream_url)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            return json_data['stream']['preview']['medium']
        else:
            return None
        
    def getStreamUrl(self):
        return "https://www.twitch.tv/" + self.channelName
    
    def getStreamImage(self):
        return "https://static-cdn.jtvnw.net/previews-ttv/live_user_" + self.channelName + "-640x360.jpg"
    
    def getStreamThumbnail(self):
        return "https://static-cdn.jtvnw.net/previews-ttv/live_user_" + self.channelName + "-80x45.jpg"
    
    def getStreamLogo(self):
        return "https://static-cdn.jtvnw.net/jtv_user_pictures/" + self.channelName + "-profile_image-300x300.png"
    
    def getStreamBanner(self):
        return "https://static-cdn.jtvnw.net/jtv_user_pictures/" + self.channelName + "-channel_offline_image-1920x1080.png"
    
    def getStreamId(self):
        twitch_api_stream_url = "https://api.twitch.tv/kraken/streams/" + self.channelName + "?client_id=" + self.clientId
        response = requests.get(twitch_api_stream_url)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            return json_data['stream']['_id']
        else:
            return None
        
    def getStreamCreatedAt(self):
        twitch_api_stream_url = "https://api.twitch.tv/kraken/streams/" + self.channelName + "?client_id=" + self.clientId
        response = requests.get(twitch_api_stream_url)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            return json_data['stream']['created_at']
        else:
            return None
        
    def getStreamUpdatedAt(self):
        twitch_api_stream_url = "https://api.twitch.tv/kraken/streams/" + self.channelName + "?client_id=" + self.clientId
        response = requests.get(twitch_api_stream_url)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            return json_data['stream']['updated_at']
        else:
            return None
        
    def getStreamDelay(self):
        twitch_api_stream_url = "https://api.twitch.tv/kraken/streams/" + self.channelName + "?client_id=" + self.clientId
        response = requests.get(twitch_api_stream_url)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            return json_data['stream']['delay']
        else:
            return None
        
    def getStreamChannelId(self):
        twitch_api_channel_url = "https://api.twitch.tv/kraken/channels/" + self.channelName + "?client_id=" + self.clientId
        response = requests.get(twitch_api_channel_url)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            return json_data['_id']
        else:
            return None
        
    def getStreamChannelName(self):
        return self.channelName
    
    def getStreamChannelDisplayName(self):
        twitch_api_channel_url = "https://api.twitch.tv/kraken/channels/" + self.channelName + "?client_id=" + self.clientId
        response = requests.get(twitch_api_channel_url)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            return json_data['display_name']
        else:
            return None
        
    def getStreamChannelGame(self):
        twitch_api_channel_url = "https://api.twitch.tv/kraken/channels/" + self.channelName + "?client_id=" + self.clientId
        response = requests.get(twitch_api_channel_url)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            return json_data['game']
        else:
            return None
        
        
