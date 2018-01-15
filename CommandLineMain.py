"""
Author: David Nester 14nesterd@gmail.com
Date: 03.01.2018

Program to Automatically mine links from reddit sport streaming sites
User chooses sport and then game and all links are presented without sorting through forums
"""
import datetime
from urllib.request import urlopen, build_opener
from bs4 import BeautifulSoup, SoupStrainer
import ssl
import re
import urllib
DOMAIN = 'https://www.reddit.com'
def get_bs(address):
    opener = build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = None
    i = 0
    while response == None and i < 10:
        try:
            response = opener.open(address)
        except:    
            pass
        i += 1
    if response == None:
        return response
    page = response.read()
    return BeautifulSoup(page, "html.parser")

class Forum:
    def __init__(self, address):
        self.address = address
        self.games = []
        self.bs = None
        
    def get_games(self):
        self.bs = get_bs(self.address)
        if self.bs == None:
            print('Error accesing page: please visit',address,'to get games')
            return
        for tag in self.bs.find_all('a', href=True, class_= 'title may-blank '):
            self.games += [Game(tag.text,DOMAIN+tag['href'])]
    
    def __str__(self):
        return self.address.split('/')[-2]

class Game:
    def __init__(self,text,address):
        self.address = address
        self.text = text
        self.bs = None
        self.web_links = []
        self.ace_links = []
    
    def get_links(self):
        self.bs = get_bs(self.address)
        if self.bs == None:
            print('Error accesing page: please visit',address,'to get links')
            return
        self.get_ace_links()
        self.get_web_links()
    
    def get_ace_links(self):
        for tag in self.bs.find_all('p'):
            if 'acestream://' in tag.text:
                self.ace_links += [tag.text]
    
    def get_web_links(self):
        for tag in self.bs.find_all('a', rel = 'nofollow', href = True):
            if 'http' in tag['href'] and 'reddit.com' not in tag['href']:
                self.web_links += [tag['href']]
    
    def __str__(self):
        return(self.text)

if __name__ == "__main__":
    SPORTS = {'Soccer':'https://www.reddit.com/r/soccerstreams/', 'College Football':'https://www.reddit.com/r/CFBStreams/', 'NFL':'https://www.reddit.com/r/nflstreams/', 'NBA':'https://www.reddit.com/r/nbastreams/', 'College Basketball':'https://www.reddit.com/r/ncaaBBallStreams/', 'NHL':'https://www.reddit.com/r/NHLStreams/', 'MLB':'https://www.reddit.com/r/MLBStreams/'}
    INDS = {1:'Soccer', 2:'College Football', 3:'NFL', 4:'NBA', 5:'College Basketball', 6:'NHL', 7:'MLB'}
    
    print('Enter sport number: ')
    for ind in INDS:
        print(ind,'::',INDS[ind])
    while True:
        try:
            ind = int(input())
            break
        except:
            print('ERROR: please give number of choice')        
    
    forum = Forum(SPORTS[INDS[ind]])
    forum.get_games()
    for i in range(len(forum.games)):
        print(i,'::', forum.games[i])
    while True:
        try:
            ind = int(input())
            break
        except:
            print('ERROR: please give number of choice')        
        
    game = forum.games[ind]
    game.get_links()
    print('ACESTREAMS')
    for st in game.ace_links:
        print(st)
    print('WEBSTREAMS')
    for st in game.web_links:
        print(st)
    
