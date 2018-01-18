from Utility import *


class Column:
    def __init__(self, master, bg):
        self.master = master
        self.bg = bg
        self.frame = Frame(master,bg=bg)
        self.buttons = []
        self.previous = None
        self.frame.pack(fill='y', side=LEFT)

    def select(self, button):
        if self.previous:
            self.previous.config(highlightbackground='white')
        button.config(highlightbackground='gray')
        self.previous = button

    def update_buttons(self, buttons, fill, pady):
        self.buttons = buttons
        for button in self.buttons:
            button.pack(fill=fill, pady=pady)

    def clear(self):
        self.frame.pack_forget()
        self.buttons = []
        self.previous = None

    def destroy(self):
        self.frame.pack_forget()
        self.frame = Frame(self.master, bg=self.bg)
        self.frame.pack(fill='y', side=LEFT)
