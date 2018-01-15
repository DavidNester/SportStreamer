from Utility import *
from Game import Game

class Forum:
    def __init__(self, address):
        self.address = address
        self.games = []
        self.bs = None

    def get_games(self):
        self.bs = get_bs(self.address)
        if self.bs is None:
            print('Error accessing page: please visit', self.address, 'to get games')
            return
        for tag in self.bs.find_all('a', href=True, class_='title may-blank '):
            if len(tag.text) < 100:  # this is really stupid
                self.games += [Game(tag.text, DOMAIN + tag['href'])]

    def __str__(self):
        return self.address.split('/')[-2]
