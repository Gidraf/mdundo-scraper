from . import mdundo_url
import requests
from bs4 import BeautifulSoup


class Artist:

    def __init__(self,letter=None):
        self.url = f"{mdundo_url}/a/"
        self.artist_url = f"{mdundo_url}/artists/all/{letter.lower()}" if letter else f"{mdundo_url}/artists"

    def get_artist(self):
        res = requests.get(self.artist_url)
        soup = BeautifulSoup(res.text, 'lxml')
        artist_wrapper = soup.find_all("div",{"class":"artist_wrapper"})
        if len(artist_wrapper) > 0:
            artist_list = artist_wrapper[0].find_all("li")
            results = []
            for artist in artist_list:
                item = {}
                item["name"] = artist.find("div",{"class" : "artist_name"}).text.strip()
                item["id"] = artist.find("div",{"class" : "artist_name"}).find("a")["href"].split("/")[-1]
                item["image"] = artist.find("img")["data-src"]
                results.append(item)
            return {"result":results,"count":len(results)}
        return []


    def get_artist_song(self, artist_id):
        if not artist_id or not artist_id.isnumeric():
            raise ValueError("Invalid artis id")
        res = requests.get(f"{self.url}{artist_id}")
        soup = BeautifulSoup(res.text, 'lxml')
        
        song_list_wrapper = soup.find_all("ul",{"id":"song_list"})
        songs_list_wrapper_hidden = None
        if len(song_list_wrapper) > 1:
            songs_list_wrapper_hidden = song_list_wrapper[1]
        if song_list_wrapper:
            artist_image = soup.find("div",{"class":"b-description__top"}).find("img")["src"]
            hidden_list = songs_list_wrapper_hidden.find_all("li") if songs_list_wrapper_hidden else []
            artist_songs = song_list_wrapper[0].find_all("li")
            all_songs = artist_songs+hidden_list
            results = []
            for song in all_songs:
                item = {}
                item["download_url"] = song.find("a",class_ = "btn btn-download")["href"]
                item["artist"] = song.find("span", class_="song-author").text
                item["genre"] = song.find("div",class_= "song-genre").text.split("/")[0].replace("#","").strip()
                item["title"] = song.find("span",class_="song-title").text
                item["image"] = artist_image
                item["source"] = song.find("a",class_ = "btn btn-play stream_play")["alt"]
                item["id"] = item["download_url"].split("/")[-1]
                results.append(item)
            return {"result":results,"count":len(results)}
        return []
