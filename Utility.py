"""
AUTHOR: David Nester
DATE: 11.01.2018

Holds all import statements, global variables, and utility functions used by SportsStreamer
"""

from urllib.request import urlopen, build_opener
from bs4 import BeautifulSoup, SoupStrainer
import ssl
import urllib
import sys
import subprocess
from tkinter import *
import webbrowser
#import praw


def open_soda_player(link):
    link = SODA_PLAYER_OPENER + link
    """Open magnet according to os."""
    if sys.platform.startswith('linux'):
        subprocess.Popen(['xdg-open', link],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elif sys.platform.startswith('win32'):
        os.startfile(link)
    elif sys.platform.startswith('cygwin'):
        os.startfile(link)
    elif sys.platform.startswith('darwin'):
        subprocess.Popen(['open', link],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        subprocess.Popen(['xdg-open', link],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def clean_ace(full_string):
    for word in full_string.split(' '):
        if word.startswith('acestream://'):
            return word
    return full_string


def get_bs(address):
    opener = build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = None
    i = 0
    while response is None and i < 10:
        try:
            response = opener.open(address)
        except:
            pass
        i += 1
    if response is None:
        return None
    page = response.read()
    return BeautifulSoup(page, "html.parser")

DOMAIN = 'https://www.reddit.com'
SODA_PLAYER_OPENER = 'sodaplayer://?url='
SPORTS = {'Soccer': 'https://www.reddit.com/r/soccerstreams/',
          'College Football': 'https://www.reddit.com/r/CFBStreams/',
          'NFL': 'https://www.reddit.com/r/nflstreams/',
          'NBA': 'https://www.reddit.com/r/nbastreams/',
          'College Basketball': 'https://www.reddit.com/r/ncaaBBallStreams/',
          'NHL': 'https://www.reddit.com/r/NHLStreams/',
          'MLB': 'https://www.reddit.com/r/MLBStreams/'}

