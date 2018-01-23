"""
Author: David Nester
Date: 1.23.2018
# Python 3.6

Class to store column of buttons. Current setup has 3 columns, sports, games, and links.
"""
from Utility import *
from scrframe import VerticalScrolledFrame


class Column:
    def __init__(self, master, bgcolor):
        self.master = master
        self.bgcolor = bgcolor
        self.frame = VerticalScrolledFrame(master, self.bgcolor)
        self.buttons = []
        self.previous = None

    def select(self, button):
        # grays out selected button and returns previous button to white
        if self.previous:
            self.previous.config(highlightbackground='white')
        button.config(highlightbackground='gray')
        self.previous = button

    def update_buttons(self, buttons, fill, pady):
        # puts new buttons in the frame
        self.buttons = buttons
        for button in self.buttons:
            button.pack(fill=fill, pady=pady)
        self.frame.pack(fill='y', side=LEFT)

    # clear and destroy may be redundant
    def clear(self):
        # removes all data from column
        self.frame.pack_forget()
        self.buttons = []
        self.previous = None

    def destroy(self):
        # Makes new frame and removes buttons
        self.frame.pack_forget()
        self.frame = VerticalScrolledFrame(self.master, self.bgcolor)
        self.buttons = []

if __name__ == "__main__":
    pass
