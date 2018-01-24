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
from tkinter import Button as OldButton
from tkinter import Frame as OldFrame
from tkinter.ttk import *
import webbrowser
from unidecode import unidecode


# from https://stackoverflow.com/a/3353112/6138243
def center(toplevel):
    # centers window on screen
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))


def message_box(message):
    # for showing an error in a new window
    r = Tk()
    # ensures box is wide enough but wraps after certain length
    width = min(len(message)*7 + 30, 830)
    dim = str(width)+'x80'
    r.geometry(dim)
    r.attributes('-topmost', True)
    r.title('Error')
    Label(r, text=message, wraplength=800).pack()
    center(r)

def open_soda_player(ace_link):
    # opens ace_link in SodaPlayer (https://www.sodaplayer.com/) or copies to clipboard if that fails
    link = SODA_PLAYER_OPENER + ace_link
    try:
        # from https://stackoverflow.com/a/47526812/6138243
        """ Open link according to os. """
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
    except:
        # copy link to clipboard
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(ace_link)
        r.update()
        r.destroy()
        message_box('Could not open SodaPlayer. AceStream link copied to clipboard.')


def clean_ace(full_string):
    # gets rid of other text included with ace link
    for word in full_string.split(' '):
        if word.startswith('acestream://'):
            return word
    return full_string


def get_bs(address):
    # gets beautiful soup object of requested page
    opener = build_opener()
    # pretends to be firefox to get access to all pages
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = None
    try:
        response = opener.open(address)
    except UnicodeEncodeError:
        response = opener.open(unidecode(address))
    except:
        pass
    if response is None:
        return None
    page = response.read()
    return BeautifulSoup(page, "html.parser")

# global variables
DOMAIN = 'https://www.reddit.com'
SODA_PLAYER_OPENER = 'sodaplayer://?url='
SPORTS = {'Soccer': 'https://www.reddit.com/r/soccerstreams/',
          'College Football': 'https://www.reddit.com/r/CFBStreams/',
          'NFL': 'https://www.reddit.com/r/nflstreams/',
          'NBA': 'https://www.reddit.com/r/nbastreams/',
          'College Basketball': 'https://www.reddit.com/r/ncaaBBallStreams/',
          'NHL': 'https://www.reddit.com/r/NHLStreams/',
          'MLB': 'https://www.reddit.com/r/MLBStreams/',
          'Golf': 'https://www.reddit.com/r/PuttStreams/',
          'Cricket': 'https://www.reddit.com/r/cricket_streams/',
          'MMA': 'https://www.reddit.com/r/MMAStreams/'}

if __name__ == "__main__":
    pass
