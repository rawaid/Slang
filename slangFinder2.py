__author__ = 'rawaid'

import os
import codecs
from collections import *


def slangFinder():
    #writing artist counts to specific artist text files
    '''
    directory = os.getcwd() + '/counts'
    if not os.path.exists(directory):
        os.makedirs(directory)
    '''
    #getting the directories
    dirDict = dirCrawl()
    print(dirDict)

    #creating the slang dictionary
    with codecs.open(os.getcwd()+'/data/slang.txt','r','utf-8', errors = 'ignore') as f:
        content = [x.strip('\r\n') for x in f.readlines()]

    cntDict = {}
    #inializing empty counter, getting counts of each slang term in each artist directory
    cnt = Counter()
    for i in range(0, len(dirDict)):
        with codecs.open(os.getcwd()+'/data/'+dirDict[i],'r','utf-8', errors = 'ignore') as file:
            print(dirDict[i])
            for line in file:
                for x in range(0,len(content)):
                    if content[x] in line.split():
                        cnt[content[x]] +=1
            #newFile = open(os.getcwd()+'/counts/'+dirDict[i][:-4]+'_count.txt', 'w')
            #newFile.write(str(cnt))
            print(cnt)
            cnt.clear()



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