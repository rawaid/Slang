__author__ = 'rawaid'
import pylast
from PyLyrics import *
import base64
import os
import codecs
from collections import *
import re
import glob
from pyechonest import config

def slangFinder():
    slangDict = {}
    countDict = {}
    with codecs.open(os.getcwd()+'/data/slang.txt','r','utf-8', errors = 'ignore') as f:
        x = 0
        for l in f:
            l = l.strip()
            slangDict[x] = l
            x += 1
    '''
    print(slangDict)
    i = 0
    for i in range (0, len(slangDict)):
        slangCounter(slangDict[i], countDict)
    print('number of terms in slang dictionary: ')
    print(len(slangDict))
    print('number of times each term comes up within lyrics: ')
    print(countDict)
    print(len(countDict))

    sorted_dict = sorted(countDict.items(), key=lambda x:x[1], reverse=True)
    print('countDict sorted greatest to least: ')
    print(sorted_dict)
    '''
    print(slangDict)
    return slangDict

    '''
    #getting files
    files = os.listdir(os.getcwd() +'/data/A Tribe Called Quest/')
    print(files)
    for z in range (0, len(files)):
        print(files[z])
    '''

    '''
    fileNum = 1
    x = 0
    slangCount = 0
    numLoops = 0
    with codecs.open(os.getcwd()+'/data/DMX/'+str(fileNum)+'.txt','r','utf-8', errors = 'ignore') as f:
        while numLoops < len(slangDict):
            for line in f:
                if slangDict[x] in line:
                    print(slangDict[x])
            x+=1
    '''


def slangCounter(slangDict,countDict):

    slangCount = 0
    #files = os.listdir(os.getcwd() +'/data/A Tribe Called Quest/')

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

    '''
    artistDict = {}
    for x in range (0,len(artists)):
        artistDict[x] = str(artists[x].item)
        if artistDict[x] == 'Run the Jewels':
            artistDict[x] = 'Run The Jewels'
        #print(artistDict[x])

    for x in range(0,len(files)):
        with codecs.open(os.getcwd()+'/data/A Tribe Called Quest/'+files[x],'r','utf-8', errors = 'ignore') as f:
            for line in f:
                if slangDict in line.split():
                    slangCount += 1
                countDict[slangDict] = slangCount
            x+=1
    '''

    dir = os.getcwd() + '/data/'
    for filename in os.listdir(dir):
        if filename == '.DS_Store':
            pass
        elif filename == 'slang.txt':
            pass
        else:
            with codecs.open(dir+filename,'r','utf-8', errors = 'ignore') as f:
                for line in f:
                    if slangDict in line.split():
                        slangCount += 1
                    countDict[slangDict] = slangCount
    return(countDict)



def dirTest(filename):
    dir = os.getcwd() + '/data/'
    for filename in os.listdir(dir):
        if filename == '.DS_Store':
            pass
        elif filename == 'slang.txt':
            pass
        else:
            with codecs.open(dir+filename,'r','utf-8', errors = 'ignore') as f:
                for line in f:
                    print(line)

def dirCrawl():
    dirDict = {}
    dir = os.getcwd() + '/data/'
    x = 0
    #while x <= 50:
    for filename in os.listdir(dir):
        if filename == '.DS_Store':
            pass
        elif filename == 'slang.txt':
            pass
        elif filename == 'artists.txt':
            pass
        else:
            dirDict[x] = filename
            x+=1

    #print(dirDict)
    countSlang(dirDict)


def countSlang(dirDict):
    countDict = {}
    slangCount = 0
    slangDict = slangFinder()

    dir = os.getcwd() + '/data/'
    print(dirDict[0])
    '''
    with codecs.open(dir+dirDict[0],'r','utf-8', errors = 'ignore') as f:
        for line in f:
            for i in range(0,len(slangDict)):
                if slangDict[i] in line.split():
                    slangCount += 1
                countDict[slangDict[i]] = slangCount
    print(countDict)
    '''





def newSlang():
    '''
    with codecs.open(os.getcwd()+'/data/slang.txt','r','utf-8', errors = 'ignore') as f:
        x = 0
        for l in f:
            l = l.strip()
            slangDict[x] = l
            x += 1
    '''

    with codecs.open(os.getcwd()+'/data/slang.txt','r','utf-8', errors = 'ignore') as f:
        content = [x.strip('\r\n') for x in f.readlines()]
    '''
    with codecs.open(os.getcwd()+'/data/2Pac.txt','r','utf-8', errors = 'ignore') as file:
        lyricContent = [text.strip() for text in file.readlines()]
    '''
    lyricContent = []
    x = 0
    cnt = Counter()
    with codecs.open(os.getcwd()+'/data/2Pac.txt','r','utf-8', errors = 'ignore') as file:
        for line in file:
            #line = line.strip()
            for x in range(0,len(content)):
                if content[x] in line.split():
                    cnt[content[x]] +=1

    print(cnt)
    '''
    print(content)
    print(len(content))

    print(lyricContent)
    print(len(lyricContent))


    cnt = Counter()
    for word in lyricContent:
        for i in range(0, len(content)):
            if content[i] in word:
                cnt[content[i]] += 1
    print(cnt)

    print(len(cnt))
    '''

    '''
    words = re.findall(r'\w+', open(os.getcwd()+'/data/2Pac.txt').read())


    myCnt = Counter(words).most_common()
    print(myCnt)
    print([content for content in myCnt if content[0]== 'aight'])
    '''





    '''
    testArray = ['blunts', 'weed']
    cnt = Counter()
    for word in testArray:
        cnt[word] += 1
    print(cnt)
    '''



    return content

#dirCrawl()
#dirTest()
#slangFinder()

newSlang()