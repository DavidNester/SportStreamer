"""
AUTHOR: David Nester
DATE: 11.01.2018

Class for a subreddit. Gets all games from reddit. Currently checks for number in post title to check if it is
a game or not. This works pretty well (catches all games) but doesnt filter out all of the other subreddit posts.
I don't worry about this too much because any user will see the difference there.
"""
from Utility import *
from Game import Game


def has_numbers(input_string):
    # from https://stackoverflow.com/a/19859308/6138243
    return any(char.isdigit() for char in input_string)


class Forum:
    def __init__(self, address):
        self.address = address
        self.games = []
        self.bs = None

    def get_games(self):
        self.bs = get_bs(self.address)
        if self.bs is None:
            message_box('Error accessing page: please visit ' + self.address + ' to get games')
            return
        for tag in self.bs.find_all('a', href=True, class_='title may-blank '):
            if has_numbers(tag.text) or 'Game Thread:' in tag.text:  # gets rid of most non-game threads
                self.games += [Game(tag.text, DOMAIN + tag['href'])]

    def __str__(self):
        return self.address.split('/')[-2]

if __name__ == "__main__":
    pass
