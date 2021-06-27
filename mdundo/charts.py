from . import mdundo_url
import requests
from bs4 import BeautifulSoup

class Chart:

    def __init__(self,country):
        if country and len(country) != 2:
            raise ValueError("Invalid Country Abbreviation")
        self.url =  f"{mdundo_url}/best/{country}" if country else f"{mdundo_url}/best"

    def weekly_top_100(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text, 'lxml')
        songs_wrapper = soup.find_all("div",{"class":"song-list_wrapper"})
        weekly_top_100 = songs_wrapper[0].find_all("li")
        results = []
        for song in weekly_top_100:
            item = {}
            item["download_url"] = song.find("a",class_ = "btn btn-download")["href"]
            item["artist"] = song.find("span", class_="song-author").text.split(".",1)[1].strip()
            item["genre"] = song.find("div",class_= "song-genre").text.split("/")[0].replace("#","").strip()
            item["title"] = song.find("span",class_="song-title").text
            item["image"] = "https://picsum.photos/200"
            item["source"] = song.find("a",class_ = "btn btn-play stream_play")["alt"]
            item["id"] = item["download_url"].split("/")[-1]
            results.append(item)
        
        return {"result":results,"count":len(results)}

    def monthly_top_20(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text, 'lxml')
        songs_wrapper = soup.find_all("div",{"class":"song-list_wrapper"})
        monthly_top = songs_wrapper[1].find_all("li")
        results = []
        for song in monthly_top:
            item = {}
            item["download_url"] = song.find("a",class_ = "btn btn-download")["href"]
            item["artist"] = song.find("span", class_="song-author").text.split(".",1)[1].strip()
            item["genre"] = song.find("div",class_= "song-genre").text.split("/")[0].replace("#","").strip()
            item["title"] = song.find("span",class_="song-title").text
            item["id"] = item["download_url"].split("/")[-1]
            item["source"] = song.find("a",class_ = "btn btn-play stream_play")["alt"]
            item["image"] = "https://picsum.photos/200"
            results.append(item)
        return {"result":results,"count":len(results)}

    def new_releases(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text, 'lxml')
        songs_wrapper = soup.find_all("div",{"class":"song-list_wrapper"})
        new_releses_song = songs_wrapper[2].find_all("li")
        results = []
        for song in new_releses_song:
            item = {}
            item["download_url"] = song.find("a",class_ = "btn btn-download")["href"]
            item["artist"] = song.find("span", class_="song-author").text
            item["genre"] = song.find("div",class_= "song-genre").text.split("/")[0].replace("#","").strip()
            item["title"] = song.find("span",class_="song-title").text
            item["id"] = item["download_url"].split("/")[-1]
            item["source"] = song.find("a",class_ = "btn btn-play stream_play")["alt"]
            item["image"] = "https://picsum.photos/200"
            results.append(item)
        return {"result":results,"count":len(results)}