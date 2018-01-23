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
        if self.previous:
            self.previous.config(highlightbackground='white')
        button.config(highlightbackground='gray')
        self.previous = button

    def update_buttons(self, buttons, fill, pady):
        self.buttons = buttons
        for button in self.buttons:
            button.pack(fill=fill, pady=pady)
        self.frame.pack(fill='y', side=LEFT)

    def clear(self):
        self.frame.pack_forget()
        self.buttons = []
        self.previous = None

    def destroy(self):
        self.frame.pack_forget()
        self.frame = VerticalScrolledFrame(self.master, self.bgcolor)
        self.buttons = []

if __name__ == "__main__":
    pass
