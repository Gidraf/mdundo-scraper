import unittest
from mdundo.artist import Artist
from string import ascii_lowercase
from mdundo import mdundo_url

class ArtistTest(unittest.TestCase):

    def test_get_artist(self):
        for c in ascii_lowercase:
            with self.subTest(i=c):
                artist = Artist(c)
                self.assertEqual(artist.artist_url, f"{mdundo_url}/artists/all/{c}")
                self.assertNotEqual(artist.get_artist(), [])
                self.assertGreater(len(artist.get_artist()), 0)

    def test_invalid_get_artist(self):
        artist = Artist("Kdfdfdfdfd")
        self.assertEqual(artist.get_artist(), [])
        self.assertEqual(len(artist.get_artist()), 0)

    def test_get_artist_song(self):
        artist = Artist()
        test_artist = artist.get_artist().get("result")[0]
        self.assertNotEqual(artist.get_artist_song(test_artist["id"]), [])
        self.assertGreater(len(artist.get_artist_song(test_artist["id"])), 0)

    def test_invalid_get_artist_song(self):
        artist = Artist()
        with self.assertRaises(ValueError):
            artist.get_artist_song("h")