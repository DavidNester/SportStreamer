"""
Author: David Nester 14nesterd@gmail.com
Date: 11.01.2018

PYTHON 3.6
Program to Automatically mine links from reddit sport streaming sites
User chooses sport and then game and all links are presented without sorting through forums
"""
from Utility import *
from Game import Game
from Forum import Forum

# TODO: Get game data
# TODO: Make links frame scrollable
# TODO: Add button to class?
# TODO: Use Reddit API?


def run():
    class Window(Frame):
        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master = master
            self.master.title("SportStreamer")
            self.master.configure(background='slate grey')
            self.game_buttons = []
            self.links = []
            self.forum = None
            self.prev_forum_button = None
            self.game = None
            self.prev_game_button = None
            self.sport_frame = Frame(self.master, bg='SeaGreen3')
            self.sport_frame.pack(anchor='w', fill='y', side=LEFT)
            self.game_frame = Frame(self.master, bg='SkyBlue3')
            self.game_frame.pack(fill='y', side=LEFT)
            self.link_frame = Frame(self.master, bg='forest green')
            self.link_frame.pack(fill='y', side=LEFT)
            for sport in SPORTS:
                button = Button(self.sport_frame, text=sport)
                button.config(command=lambda address=SPORTS[sport], but=button: self.sport_click(but,address))
                if self.forum is None:
                    temp_button = button
                    self.forum=Forum(SPORTS['Soccer'])
                button.pack(fill='x')
            self.sport_click(temp_button)
            
        def sport_click(self, button, address=SPORTS['Soccer']):
            if self.prev_forum_button:
                self.prev_forum_button.config(highlightbackground='white')
            button.config(highlightbackground='gray')
            self.prev_forum_button = button
            self.forum = Forum(address)
            self.forum.get_games()
            self.game_frame.pack_forget()
            self.link_frame.pack_forget()
            self.game_buttons = []
            self.game_frame = Frame(self.master, bg='SkyBlue3')
            self.game_frame.pack(fill='y', side=LEFT)
            self.links = []
            self.link_frame = Frame(self.master, bg='forest green')
            self.link_frame.pack(fill='y', side=LEFT)
            for game in self.forum.games:
                temp_button = Button(self.game_frame, text=game.text)
                temp_button.config(command=lambda g=game, but=temp_button: self.game_click(g, but))
                self.game_buttons += [temp_button]
            self.draw()

        def game_click(self, game, button):
            if self.prev_game_button:
                self.prev_game_button.config(highlightbackground='white')
            button.config(highlightbackground='gray')
            self.prev_game_button = button
            self.links = []
            self.link_frame.pack_forget()
            self.link_frame = Frame(self.master, bg='forest green')
            self.link_frame.pack(fill='y', side=LEFT)
            self.game = game
            game.get_links()
            self.links += [Label(self.link_frame, text='ACESTREAMS')]
            for ace in game.ace_links:
                link = Button(self.link_frame, text=ace, fg='blue', cursor='hand2')
                link.config(command=lambda but=link,l=clean_ace(ace): self.open_link(but,l))
                self.links += [link]
            self.links += [Label(self.link_frame, text='WEB STREAMS')]
            for web in game.web_links:
                link = Button(self.link_frame, text=web, fg='blue', cursor='hand2')
                link.config(command=lambda but=link, l=web: self.open_link(but,l))
                self.links += [link]
            self.draw()

        def open_link(self,button,link):
            button.config(highlightbackground='gray')
            if 'acestream://' in link:
                open_soda_player(link)
            else:
                webbrowser.open_new_tab(link)

        def draw(self):
            # draw game buttons
            for button in self.game_buttons:
                button.pack()
            # draw links
            for link in self.links:
                link.pack()

        def client_exit(self):
            exit()

    root = Tk()
    root.geometry("1200x800")
    app = Window(root)

    root.mainloop()

if __name__ == "__main__":
    run()
