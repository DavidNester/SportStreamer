"""
AUTHOR: David Nester
DATE: 11.01.2018

Class for a Game (a post in a subreddit). Goes through the page and gets all acestream links and all external links to
web pages. This method is not perfect for the web links because there are occasionally links to other things but it
has been pretty successful in my experience so far.
"""
from Utility import *


class Game:
    def __init__(self, text, address):
        self.address = address
        self.text = text
        self.bs = None
        self.web_links = []
        self.ace_links = []

    def get_links(self):
        self.bs = get_bs(self.address)
        if self.bs is None:
            message_box('Error accessing page: please visit ' + self.address + ' to get links')
            return
        self.get_ace_links()
        self.get_web_links()

    def get_ace_links(self):
        self.ace_links = []
        for tag in self.bs.find_all('p'):
            if 'acestream://' in tag.text:
                self.ace_links += [tag.text]

    def get_web_links(self):
        self.web_links = []
        # added because it wasn't catching links from grandma streams (usually pretty high quality)
        for tag in self.bs.find_all('a', href=True):
            if 'grandma' in tag['href'] and 'donate' not in tag['href']:
                self.web_links += [tag['href']]
        for tag in self.bs.find_all('a', rel='nofollow', href=True):
            if 'http' in tag['href'] and 'reddit.com' not in tag['href'] and '.png' not in tag['href']:
                self.web_links += [tag['href']]

    def __str__(self):
        return self.text

if __name__ == "__main__":
    pass
