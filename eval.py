__author__ = 'rawaid'
import os
import codecs
from math import *
from collections import *
import sqlite3

def eval():
    countDirDict = countCrawl()
    print(countDirDict)
    for c in range(21,len(countDirDict)):
        countDict = getCount(countDirDict[c])
        wordDict = getWords(countDirDict[c])



        weightDict = {}
        for i in range(0, len(wordDict)):
            item = wordDict[i].replace("'","")

            docFreq = numTimesInDocs(item)
            tfIDF = (1 * log(float(countDict[i])))* log(48/docFreq)
            weightDict[i] = tfIDF
            print('tf-idf for ' + str(item) + ' is ' + str(tfIDF))

        print(weightDict)

        sum = 0
        for x in range(0, len(weightDict)):
            weightDict[x] = weightDict[x] * weightDict[x]
            sum += weightDict[x]

        normalizedScore = sqrt(sum)
        print('Normalized score is ' + str(normalizedScore))

        file_path = os.getcwd() + '/weights/' + countDirDict[c].replace('.txt', '_normalized.txt')
        myFile = open(file_path, "w", encoding = 'utf-8')

        for j in range (0,len(weightDict)):
            weightDict[j] = weightDict[j]/normalizedScore
            print('final weight for ' + str(wordDict[j]) + ' is ' + str(weightDict[j]))
            myFile.write('final weight for ' + str(wordDict[j]) + ' is ' + str(weightDict[j]) + '\n')


    return

def getCount(countItem):
    countDict = {}
    x = 0
    #with codecs.open(os.getcwd()+'/fixedCounts/Wu-Tang Clan_count.txt','r','utf-8', errors = 'ignore') as f:
    with codecs.open(os.getcwd()+'/fixedCounts/' + countItem,'r','utf-8', errors = 'ignore') as f:

        for line in f:
            #print(line)
            new_str = ''.join(line.strip(',\n').split(':')[1:])
            countDict[x] = new_str
            #countDict[i] = line.strip("\n,")
            x+=1
    #print('COUNT DICT:')
    #print(countDict)


   # for j in range(0, len(countDict)):
    #    print('2pac says ' + wordDict[j] + countDict[j] + ' times')
    return countDict


def getWords(countItem):
    #with codecs.open(os.getcwd()+'/counts/2Pac_count copy.txt','r','utf-8', errors = 'ignore') as f:
    #    content = [x.strip().split() for x in f.readlines()]

    i = 0
    wordDict = {}
    #with codecs.open(os.getcwd()+'/counts/2Pac_count copy.txt','r','utf-8', errors = 'ignore') as f:
    with codecs.open(os.getcwd()+'/fixedCounts/' + countItem,'r','utf-8', errors = 'ignore') as f:

        for line in f:
            #print(line)
            new_str = ''.join(line.split(':')[:1])
            new_str.strip()
            wordDict[i] = new_str
            #countDict[i] = line.strip("\n,")
            i+=1
   # print('WORD DICT:')
  #  print(wordDict)
    return wordDict

def numTimesInDocs(searchWord):
    print(searchWord.strip(''))
    dirDict = dirCrawl()
    numTimes = 0
    for i in range(0, len(dirDict)):
        with codecs.open(os.getcwd()+'/data/'+dirDict[i],'r','utf-8', errors = 'ignore') as file:
            word_list = []
            for line in file:
                word_list.append(line.split())
            if any(searchWord in s for s in word_list):
                numTimes += 1
    #print(numTimes)
    return numTimes

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


    return(dirDict)

def countCrawl():
    countDirDict = {}
    dir = os.getcwd() + '/fixedCounts/'
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
            countDirDict[x] = filename
            x+=1

    print(countDirDict)
    return(countDirDict)


#eval()
#dirCrawl()

eval()
