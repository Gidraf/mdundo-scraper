from . import mdundo_url
import requests
from bs4 import BeautifulSoup


class Genre:

    def __init__(self):
        self.genre_url =  f"{mdundo_url}/best"
        self.url = f"{mdundo_url}/genres"

    def get_genres(self):
        res = requests.get(self.genre_url)
        soup = BeautifulSoup(res.text, 'lxml')
        genre_wrapper = soup.find("div",{"class":"heading_select"})
        genre_options = genre_wrapper.find_all("option")
        results = []
        for genre in genre_options:
            value = genre["value"]
            genre_id = value.split("/")[-1]
            if genre_id.isnumeric():
                item = {}
                item["id"] = genre_id
                item["name"] = genre.text
                results.append(item)
        return {"result":results,"count":len(results)}


    def get_genre_top_songs(self, genre_id):
        if not genre_id or not genre_id.isnumeric():
            raise ValueError("Invalid Id")
        res = requests.get(f"{self.url}/{genre_id}")
        soup = BeautifulSoup(res.text, 'lxml')
        songs_wrapper = soup.find_all("div",{"class":"song-list_wrapper"})
        if len(songs_wrapper) > 0:
            genre_songs = songs_wrapper[0].find_all("li")
            results = []
            for song in genre_songs:
                item = {}
                item["source"] = song.find("a",class_ = "btn btn-download")["href"]
                item["artist"] = song.find("span", class_="song-author").text.split(".",1)[1].strip()
                item["genre"] = song.find("div",class_= "song-genre").text.split("/")[0].replace("#","").strip()
                item["title"] = song.find("span",class_="song-title").text
                item["id"] = item["source"].split("/")[-1]
                results.append(item)
            return {"result":results,"count":len(results)}
        return []
