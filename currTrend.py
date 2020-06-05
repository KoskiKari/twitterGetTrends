import tweepy
import time
import datetime
import os 

def auth():
    #finding creditentials from a file and saving them in a list
    creditentials = []
    creditPath = 'D:\\misc\\currentTrendsFinder\\currentTrendsFinderCreds.txt'
    with open (creditPath,'r') as f:
        for i in f:
            creditentials.append(i.split()[-1][1:-1]) #getting rid of the extra stuff on the row

    auth = tweepy.OAuthHandler(creditentials[0], creditentials[1])  #consumer_key, consumer_secret
    auth.set_access_token(creditentials[2], creditentials[3])       #access_token, access_secret
    api = tweepy.API(auth)
    return api

def getTrends():
    api = auth()

    trendsObject = api.trends_place(1)
    #try to understand why this works, and simplify / optimize
    data = trendsObject[0]
    trendList = data['trends']
    #get trends by "name"
    trendNames = [name['name'] for name in trendList]
    print(trendNames)
    writeTrendsToFile(trendNames)

def writeTrendsToFile(trendNames):
    fileExtension = getNewFilename() #get filename from datetime timestamp
    filename = 'D:\\misc\\currentTrendsFinder\\trendTexts\\trends' + fileExtension +'.txt'
    with open(filename,'w',encoding='utf8') as f:
        for i in trendNames:
            try:
                f.write(f'{i}\n')
            except:
                #Should never enter here anymore, encoding with file from open
                f.write(f'{i.encode("utf-8")}\n')
                print(f'UTF-8 Encoding: {i}')

def getNewFilename():
    fileExtension = str(datetime.datetime.now().date()) + '_'
    #using strftime to dump datetime as str, and preserving the leading zeroes (eg 08 instead of 8)
    fileExtension += str(datetime.datetime.now().strftime("%H"))  + '-'
    fileExtension += str(datetime.datetime.now().strftime("%M"))
    return fileExtension

def sleepCycle():
    cycles = 60        #cycles * timePerCycle = fullSleepTime
    timePerCycle = 6
    endTime = cycles * timePerCycle

    print('*** SLEEP CYCLE START ***')
    print('Seconds slept: 0 /', endTime, end='\r')
    for i in range(cycles): 
        time.sleep(timePerCycle)
        print('Seconds slept:', (i+1)*timePerCycle, '/', endTime, end='\r')
    print('*** NEXT CYCLE *** NEXT CYCLE *** NEXT CYCLE ***')

while True:
    getTrends()
    sleepCycle()