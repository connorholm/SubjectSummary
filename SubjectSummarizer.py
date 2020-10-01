#Program makes a short summary or topic headlines for the users choosen subject
#Uses webscraping tools BeautifulSoup and request
#Data is collected from Wikipedia

from bs4 import BeautifulSoup
import requests

#Creates the summary
#For returnType use an int 0,1,2
#0 returns nothing, 1 returns summary, 2 returns the headlines of the subject
def parseData(topic, returnType):
    subject = topic
    Headlines = []
    paragraphs = []

    #Gets the website and puts it into a document to be parsed using BeatifulSoup
    url = "https://en.wikipedia.org/wiki/{subject}".format(subject= subject)
    r = requests.get(url)

    #Parsing through the website using BeatifulSoup
    soup = BeautifulSoup(r.text, "html.parser")
    result = soup.find(class_="mw-parser-output")
    narrowed = result.find_all(class_="mw-headline")
    divFinder = soup.find(class_="mw-parser-output")
    pFinderArray = divFinder.find_all("p")
    for paragraph in pFinderArray:
        if paragraph.get_text() == "\n":
           continue
        paragraphs.append(paragraph.get_text())
    for texts in narrowed:
        Headlines.append(texts.get_text())
    #Takes the summary containing the "[#]" and removes it from the summary
    jumbledSummary = paragraphs[0]
    summaryIndex = 0
    for character in jumbledSummary:
        if character == "[":
            jumbledSummary = jumbledSummary[0: summaryIndex] + jumbledSummary[summaryIndex+3:]
            summaryIndex-=3
        summaryIndex+=1
    summary = jumbledSummary
    if returnType == 0:
        return ""
    elif returnType == 1:
        return summary
    elif returnType == 2:
        return Headlines
    




#Creates getter methods
def getHeadlines(topic):
    return parseData(topic, 2)

def getSummary(topic):
    return parseData(topic, 1)

#Gets the users desired subject to find summary
def userSubject():
    return input("Get summary of any person/place/thing\nDesired subject: ")

#Displaying the different headlines
if __name__ == "__main__":
    subject = userSubject()
    print("\n{summary}".format(summary=getSummary(subject)))