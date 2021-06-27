import unittest
from mdundo.genre import Genre
from string import ascii_lowercase
from mdundo import mdundo_url


class GenreTest(unittest.TestCase):

    def setUp(self):
        self.genre = Genre()

    def test_get_genres(self):
        self.assertNotEqual(self.genre.get_genres(),[])

    def test_get_genre_top_songs(self):
        test_genre = self.genre.get_genres()["result"][0]
        self.assertNotEqual(self.genre.get_genre_top_songs(test_genre.get("id")),[])

    def test_invalid_get_genre_top_songs(self):
        with self.assertRaises(ValueError):
            self.genre.get_genre_top_songs("h")