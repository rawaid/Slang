import pylast
from PyLyrics import *
import base64
# LYRICSnMUSIC Api Key = 29af6fae353173522c2aab3c3e655d
def spider():
    #Last.FM API:
    # You have to have your own unique two values for API_KEY and API_SECRET
    # Obtain yours from http://www.last.fm/api/account for Last.fm
    API_KEY = "79e56e21872143d086778ef7bc0f7c5d" # this is a sample key
    API_SECRET = "22bb0a5590e7dbb391f88a0657648838"
    decoded = base64.b64decode(b'YWZyb3p5YWtuMHd6Pw==')
    decoded = str(decoded)
    decoded = decoded[2:-1]

    '''
    #EchoNest API:
    config.ECHO_NEST_API_KEY="K9GHS1ZS13C6ASJBH"
    '''

    # In order to perform a write operation you need to authenticate yourself
    username = "rawaid"
    password_hash = pylast.md5(decoded)





    network = pylast.LastFMNetwork(api_key = API_KEY, api_secret =
        API_SECRET, username = username, password_hash = password_hash)

    # now you can use that object every where

    #assigning the rap tag, getting all of the top artists
    tag = network.get_tag("rap")
    artists = tag.get_top_artists()

    '''
    art = artists[0].item
    tracks = art.get_top_tracks()
    print(tracks)
    trackDict = {}
    for x in range(0,len(tracks)):
        trackDict[x] = str(tracks[x].item)
        print(trackDict[x])
    '''
    artistDict = {}

    for x in range(0, 2):
        #print(artists[x].item)
        artistDict[x] = str(artists[x].item)
        print(artistDict[x])
        count = 0
        track = artists[x].item.get_top_tracks()
        trackDict = {}
        for x in range(0, len(track)):
            trackDict[x] = str(track[x].item)

            count += 1
            print(trackDict[x])

    print('\n')


      #  albums = PyLyrics.getAlbums(singer = artistDict[x])


    print(PyLyrics.getLyrics(artistDict[1], 'Bound 2'))



    print('')



    #print(PyLyrics.getLyrics('Taylor Swift','Blank Space'))

    # type help(pylast.LastFMNetwork) or help(pylast) in a python interpreter to get more help
    # about anything and see examples of how it works
    return

spider()

'''
 def test_tag_top_artists(self):
        # Arrange
        tag = self.network.get_tag("blues")

        # Act
        artists = tag.get_top_artists(limit=1)

        # Assert
        self.helper_only_one_thing_in_top_list(artists, pylast.Artist)
'''