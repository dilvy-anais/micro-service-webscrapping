import requests
from bs4 import BeautifulSoup
import json
import re

class Scraper:
    _infos = {
        'videoId': '',
        'title': '',
        'author': '',
        'description': '',
        'like': 0,
        'links' : []
        #        'comments': []
    }
    content: str

    def __init__(self, url: str):
        response = requests.get(url)
        if response.ok:
            self.content = BeautifulSoup(response.content, "html.parser")
        else:
            self.content = None


    def get_all(self)->dict:
            self.get_standard_infos()
            self.get_like()
            self.find_link()
            return self._infos

    def get_standard_infos(self)->None:
        string_data = self.content.find("body").findChild("script").text.replace("var ytInitialPlayerResponse = ", '').replace(';','')
        json_data = json.loads(string_data)
        self._infos["description"] = json_data["videoDetails"]["shortDescription"]
        self._infos['author'] = json_data["videoDetails"]["author"]
        self._infos["videoId"] = json_data["videoDetails"]["videoId"]
        self._infos["title"] = json_data["videoDetails"]["title"]


    def get_like(self)->None:
        string_data = self.content.findAll("script")[-5].text.replace('var ytInitialData = ',"").replace(";","")
        json_data = json.loads(string_data)
        like_sentence = json_data["contents"]["twoColumnWatchNextResults"]["results"]["results"]["contents"][0]["videoPrimaryInfoRenderer"]["videoActions"]["menuRenderer"]["topLevelButtons"][0]['segmentedLikeDislikeButtonRenderer']["likeButton"]["toggleButtonRenderer"]["accessibility"]["label"]
        self._infos["like"] = int("".join([temp for temp in like_sentence.split() if temp.isdigit()]))

    def find_link(self)->None:
        if self._infos["description"]!='':
            self._infos["links"] = re.findall(r'(https?://[^\s]+)', self._infos["description"])












