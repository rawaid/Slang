__author__ = 'rawaid'
import pylast
from PyLyrics import *
import base64
import os
import errno
import codecs
import pkgutil
import re
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

    print(slangDict)
    i = 0
    for i in range (0, len(slangDict)):
        slangCounter(slangDict[i], countDict)

    print(countDict)
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
    fileNum = 1
    slangCount = 0

    with codecs.open(os.getcwd()+'/data/DMX/' + str(fileNum) +'.txt','r','utf-8', errors = 'ignore') as f:
        for line in f:
            if slangDict in line:
                slangCount += 1
            countDict[slangDict] = slangCount

    return(countDict)








slangFinder()
