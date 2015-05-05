__author__ = 'rawaid'
import pylast
from PyLyrics import *
import base64
import os
import errno
import codecs
import pkgutil
from pyechonest import config
import time

def tracks(artist):

   # for i in range(0,len(artistDict)):
    albums = PyLyrics.getAlbums(singer=artist)
    #print(artistDict[i] + "'s total albums: ")
   # print(len(albums))


    numTracks = 0
    file_path = os.getcwd()+'/data/'+artist+'.txt'
    f = open(file_path, 'w', encoding='utf-8')
    for i in range(0,len(albums)):
        myAlbum = albums[i]
        try:
            tracks = myAlbum.tracks()
        except UnboundLocalError:
            pass
        for track in tracks:
            try:
                lyrics = track.getLyrics()
                lyrics = lyrics.lower()
                lyrics = lyrics.replace("!", "")
                lyrics = lyrics.replace(",", "")
                lyrics = lyrics.replace(".", "")
                lyrics = lyrics.replace("'", "")
                lyrics = lyrics.replace("(", "")
                lyrics = lyrics.replace(")", "")
                lyrics = lyrics.replace("?", "")
                lyrics = lyrics.replace('"', "")
                lyrics = lyrics.replace(":", "")
                print(lyrics)
                f.write(lyrics)
                numTracks += 1
            except (ValueError, UnboundLocalError):
                pass
    print('total number of tracks printed: ' + str(numTracks))


def getWords():
    #SETUP - last.fm/echonest authentication
    API_KEY = "79e56e21872143d086778ef7bc0f7c5d" # this is a sample key
    API_SECRET = "22bb0a5590e7dbb391f88a0657648838"
    decoded = base64.b64decode(b'YWZyb3p5YWtuMHd6Pw==')
    decoded = str(decoded)
    decoded = decoded[2:-1]
    #EchoNest API:
    config.ECHO_NEST_API_KEY="K9GHS1ZS13C6ASJBH"
    # In order to perform a write operation you need to authenticate yourself
    username = "rawaid"
    password_hash = pylast.md5(decoded)
    network = pylast.LastFMNetwork(api_key = API_KEY, api_secret =
        API_SECRET, username = username, password_hash = password_hash)

    # Creating artist dict
    tag = network.get_tag("rap")
    artists = tag.get_top_artists()

    artistDict = {}
    for x in range (0,len(artists)):

        artistDict[x] = str(artists[x].item)
        if artistDict[x] == 'Run the Jewels':
            artistDict[x] = 'Run The Jewels'
        print(artistDict[x])

    for i in range(44, len(artistDict)):
        print('writing ' + artistDict[i] + "'s lyrics.")
        tracks(artistDict[i])
    '''
    for i in range(0,50):
        try:
            print('Writing' + artistDict[i] + "'s Lyrics.")
            tracks(artistDict[i])
        except UnboundLocalError:
            pass
    '''
#tracks('Wu-Tang Clan')

getWords()
