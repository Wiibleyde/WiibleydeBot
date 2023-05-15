from .config import ConfigService

import requests

class YoutubeService:
    def __init__(self):
        self.channelName = ConfigService('config.yaml').getYoutubeChannel()
        self.apiKey = ConfigService('config.yaml').getYoutubeApiKey()

    def hasChannelNewVideo(self):
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={self.channelName}&type=video&key={self.apiKey}&maxResults=1'
        response = requests.get(url).json()
        if len(response['items']) == 0:
            return False
        else:
            return True
        
    def getChannelNewVideoInfo(self):
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={self.channelName}&type=video&key={self.apiKey}&maxResults=1'
        response = requests.get(url).json()
        return response['items'][0]
    
    def getChannelNewVideoTitle(self):
        return self.getChannelNewVideoInfo()['snippet']['title']
    
    def getChannelNewVideoDescription(self):
        return self.getChannelNewVideoInfo()['snippet']['description']
    
    def getChannelNewVideoThumbnail(self):
        return self.getChannelNewVideoInfo()['snippet']['thumbnails']['high']['url']
    
    def getChannelNewVideoUrl(self):
        return f'https://www.youtube.com/watch?v={self.getChannelNewVideoInfo()["id"]["videoId"]}'
    
    def getChannelNewVideoPublishedAt(self):
        return self.getChannelNewVideoInfo()['snippet']['publishedAt']
    
    def getChannelNewVideoChannelId(self):
        return self.getChannelNewVideoInfo()['snippet']['channelId']
    
    def getChannelNewVideoChannelTitle(self):
        return self.getChannelNewVideoInfo()['snippet']['channelTitle']
    
    def getChannelNewVideoLiveBroadcastContent(self):
        return self.getChannelNewVideoInfo()['snippet']['liveBroadcastContent']
    
    def getChannelNewVideoTags(self):
        return self.getChannelNewVideoInfo()['snippet']['tags']
    
    def getChannelNewVideoCategoryId(self):
        return self.getChannelNewVideoInfo()['snippet']['categoryId']
    
    def getChannelNewVideoViewCount(self):
        return self.getChannelNewVideoInfo()['snippet']['viewCount']
    
    def getChannelNewVideoLikeCount(self):
        return self.getChannelNewVideoInfo()['snippet']['likeCount']
    
    def getChannelNewVideoDislikeCount(self):
        return self.getChannelNewVideoInfo()['snippet']['dislikeCount']
    
    def getChannelNewVideoCommentCount(self):
        return self.getChannelNewVideoInfo()['snippet']['commentCount']
    
    def getChannelNewVideoDuration(self):
        return self.getChannelNewVideoInfo()['snippet']['duration']