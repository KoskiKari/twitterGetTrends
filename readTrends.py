import glob
import itertools

def getFilenames():
    path = 'D:\\misc\\currentTrendsFinder\\trendTexts\\'

    #with list comprehension
    txtFiles = [txt for txt in glob.glob(path+'*.txt')]

    #opened in for loop
    txtFiles = []
    for txt in glob.glob(path + '*.txt'):
        txtFiles.append(txt)

    return txtFiles

def readTrends(txtFiles):

    trends = []
    for filename in txtFiles:
        if 'currentTrendsFinderCreds.txt' in filename:
            continue
        with open (filename,'r',encoding='utf8') as f:
            for i in f:
                try:
                    trends.append(i)
                    #print(i.strip())
                except:
                    #redundant as of now, keeping it here as a reminder 
                    print('***Exception***')
                    utfStr = bytes([ord(c) for c in i.split('\'')[1]])
                    print(utfStr.decode())
    return trends

def formatTrends(trends):
    trendNumbers = []
    trends.sort() #sorting the list for use with groupby

    #groupby from itertools to count number of occurences
    for key, grouper in itertools.groupby(trends):
        groupLength = len(list(grouper))
        trendNumbers.append([key.strip(), groupLength])

    #sort by second column
    sortedTrends = sorted(trendNumbers, key=lambda x: x[1], reverse=True)

    for i in sortedTrends:
        print(i)

txtFiles = getFilenames()
trends = readTrends(txtFiles)
formatTrends(trends)