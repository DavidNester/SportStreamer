from Utility import *
from scrframe import *

def MouseWheelHandler(event):
    global count

    def delta(event):
        if event.num == 5 or event.delta < 0:
            return -1
        return 1

    count += delta(event)
    print(count)

class Column:
    def __init__(self, master, style):
        self.master = master
        self.style = style
        #self.frame = Frame(master,bg=bg)
        self.frame = VerticalScrolledFrame(master,self.style)
        self.buttons = []
        self.previous = None
        if len(self.buttons) > 0:
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
        if len(self.buttons) > 0:
            self.frame.pack(fill='y', side=LEFT)

    def clear(self):
        self.frame.pack_forget()
        self.buttons = []
        self.previous = None

    def destroy(self):
        self.frame.pack_forget()
        #self.frame = Frame(self.master, bg=self.bg)
        self.frame = VerticalScrolledFrame(self.master,self.style)
        self.buttons = []
        if len(self.buttons) > 0:
            self.frame.pack(fill='y', side=LEFT)
