__author__ = 'rawaid'

import os
import codecs
from collections import *

def slangFinder():

    dirDict = dirCrawl()
    print(dirDict)

    with codecs.open(os.getcwd()+'/data/slang.txt','r','utf-8', errors = 'ignore') as f:
        content = [x.strip('\r\n') for x in f.readlines()]


    cnt = Counter()
    with codecs.open(os.getcwd()+'/data/2Pac.txt','r','utf-8', errors = 'ignore') as file:
        for line in file:
            #line = line.strip()
            for x in range(0,len(content)):
                if content[x] in line.split():
                    cnt[content[x]] +=1

    print(cnt)


    return cnt

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


    return dirDict

slangFinder()