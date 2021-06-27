# Mdundo Scraper

## Get songs data in json format from [Mdundo site](mdundo.com) with ease inspired by [Sound Cloud Scraper](https://soundcloud-scraper.js.org/).

<br>

# Installation

 ` pip install mdundo-scraper `

 # Usage

 ## Charts
 ```
 from mdundo.charts import Chart

  # Initialize Chart class

  chart = Chart("ke") 
  
 # Weekly top 100 songs

  top_100_songs = chart.weekly_top_100(chart)

 # Top 20 monthly songs

  top_20_songs = chart.monthly_top_20(chart)

 # New Releases
  new_relases_songs = chart.new_releases(chart)

 ```

  ## Genre
 ```
 from mdundo.genre import Genre

  # Initialize Genre class

  genre = Genre() 
  
 # All Genres

 all_genres = genre.get_genres()

 # Songs in a genre
  
  genre = genre.get_genre_top_songs(genre_id)

 ```

  ## Artist
 ```
 from mdundo.artist import Artist

  # Initialize Artist class

  genre = Artist() 
  
 # top artist

 top_artist = genre.get_artist()

 # Get Artist's Songs
  
  songs = artist.get_artist_song(artist_id)

 ```

 ***
 To see how you can implement this package in a real life project have a look at examples.py. Contains a flask implementation of this project.

 This repo show you how you can consume the API created with your server with an android client.
  ***

  ***
  # Note
  This package is a project that I am using to learn data science and how audio waves can be manipulated and is in no way affiliated with Mdundo.com. Use at your own discretion.
  ***


