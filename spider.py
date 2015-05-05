import pylast
from PyLyrics import *
import base64
import os
import errno
import codecs
import pkgutil
from pyechonest import config
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


    #EchoNest API:
    config.ECHO_NEST_API_KEY="K9GHS1ZS13C6ASJBH"


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

    #Getting the slang dictionary, reading from file and creating Dict.
    slangDict = {}
    with codecs.open(os.getcwd()+'/data/slang.txt','r','utf-8', errors = 'ignore') as f:
        for l in f:
            l = l.strip()
            for x in range (0, 193):
                slangDict[x] = l
            print(slangDict[x])

    '''
    #writing all artists to a file
    file_path = os.getcwd()+ "/data/artists.txt"
    f = open(file_path, "w", encoding = 'utf-8')

    for i in range(0,len(artists)):
        artistDict[i] = str(artists[i].item)
        f.write(artistDict[i]+'\n')
    '''


    '''
    for x in range(0, len(artists)):
        #print(artists[x].item)
        artistDict[x] = str(artists[x].item)

        #Creating directories for every artist if they don't yet exist
        path = os.getcwd()
        try:
            os.makedirs(path + '/data' + '/' + artistDict[x])
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

        print(artistDict[x],"'s tracks:")
        count = 0
        track = artists[x].item.get_top_tracks()
        trackDict = {}

        trackCount = 0

        for x in range(0, len(track)):
            trackCount +=1
            trackDict[x] = str(track[x].item)

            print(trackCount, trackDict[x])


           # count += 1
            #print(trackDict[x])



        for x in range(0,len(artists)):
            artistDict[x] = str(artists[x].item)
            for j in range(0, len(track)):
                if artistDict[x] in trackDict[j]:
                    count += 1

                    file_path = "data/" + artistDict[x] + "/" + str(count) + ".txt"
                    try:
                        f = open(file_path, "w", encoding = 'utf-8')
                    except FileNotFoundError:
                        pass

                    length = len(artistDict[x])
                    trackDict[j] = trackDict[j][length +3:]
                    try:
                        #print(PyLyrics.getLyrics(artistDict[x], trackDict[j]))
                        lyrics = str(PyLyrics.getLyrics(artistDict[x], trackDict[j]))
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

                        f.write(lyrics)
                    except ValueError:
                        pass


        print('')

'''










    #print(PyLyrics.getLyrics('Taylor Swift','Blank Space'))

    # type help(pylast.LastFMNetwork) or help(pylast) in a python interpreter to get more help
    # about anything and see examples of how it works
    return
def make_sure_path_exists():
    path = os.getcwd()
    try:
        os.makedirs(path + '/data')
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

make_sure_path_exists()
spider()
