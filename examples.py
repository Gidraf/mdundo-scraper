from mdundo.charts import Chart
from mdundo.genre import Genre
from mdundo.artist import Artist
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/weekly")
def get_weekly_charts():
    country = request.args.get("country")
    chart = Chart(country)
    return jsonify(Chart.weekly_top_100(chart))

@app.route("/monthly")
def get_monthly_charts():
    country = request.args.get("country")
    chart = Chart(country)
    return jsonify(Chart.monthly_top_20(chart))

@app.route("/new_releases")
def get_new_charts():
    country = request.args.get("country")
    chart = Chart(country)
    return jsonify(Chart.new_releases(chart))

@app.route("/available_genres")
def get_available_genres():
    genre = Genre()
    return jsonify(genre.get_genres())

@app.route("/genre_songs")
def get_genre_songs():
    genre_id = request.args.get("id")
    genre = Genre()
    return jsonify(genre.get_genre_top_songs(genre_id))

@app.route("/artist")
def get_artist():
    letter = request.args.get("letter")
    artist = Artist(letter) 
    return jsonify(artist.get_artist())


@app.route("/artist_songs")
def get_artist_songs():
    artist_id = request.args.get("id")
    artist = Artist() 
    return jsonify(artist.get_artist_song(artist_id))


if __name__ == "__main__":
    app.run(debug=True, port=6000)

