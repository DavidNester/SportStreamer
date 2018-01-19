from Utility import *
from Game import Game


def hasNumbers(inputString):
    #from https://stackoverflow.com/a/19859308/6138243
    return any(char.isdigit() for char in inputString)


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
            if hasNumbers(tag.text):  # gets rid of most non-game threads
                self.games += [Game(tag.text, DOMAIN + tag['href'])]

    def __str__(self):
        return self.address.split('/')[-2]
