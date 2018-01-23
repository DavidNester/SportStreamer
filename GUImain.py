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
from Column import Column

# TODO: Get game data
# TODO: Make links frame scrollable
# TODO: Add button to class?
# TODO: Use Reddit API?
# TODO: Chromecast --> https://github.com/balloob/pychromecast
# TODO: Handle improper characters

def run():
    class Window(Frame):
        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master = master
            self.master.title("SportStreamer")
            self.master.configure(background='slate grey')
            self.forum = None
            self.game = None
            self.Sports = Column(self.master, 'SeaGreen3')
            self.Games = Column(self.master, 'SkyBlue3')
            self.Links = Column(self.master, 'forest green')
            self.make_sport_buttons()

        def make_sport_buttons(self):
            buttons = []
            temp_button = None
            for sport in SPORTS:
                button = OldButton(self.Sports.frame.interior, text=sport,pady=10)
                button.config(command=lambda address=SPORTS[sport], but=button: self.sport_click(but, address))
                if temp_button is None:
                    temp_button = button
                buttons += [button]
            self.Sports.update_buttons(buttons,'x',10)
            self.sport_click(temp_button, SPORTS['Soccer'])
            
        def sport_click(self, button, address):
            self.Sports.select(button)
            self.Links.destroy()
            self.Games.destroy()
            self.forum = Forum(address)
            self.forum.get_games()
            buttons = []
            for game in self.forum.games:
                temp_button = OldButton(self.Games.frame.interior, text=game.text,pady=5,padx=2)
                temp_button.config(command=lambda g=game, but=temp_button: self.game_click(g, but))
                buttons += [temp_button]
            if not buttons:
                buttons += [OldButton(self.Games.frame.interior, text='No Games Found. Click to visit forum.', pady=5,
                                   command=lambda add=address: webbrowser.open_new_tab(add))]
            self.Games.update_buttons(buttons,'x',5)

        def game_click(self, game, button):
            self.Games.select(button)
            self.Links.destroy()
            self.game = game
            self.game.get_links()
            links = []
            links += [Label(self.Links.frame.interior, text='ACESTREAMS', background='gold', relief=GROOVE)]
            for ace in game.ace_links:
                #link = Button(self.Links.frame, text=ace, fg='blue', cursor='hand2', pady=2)
                link = OldButton(self.Links.frame.interior, text=ace, cursor='hand2', pady=2)
                link.config(command=lambda but=link,l=clean_ace(ace): self.open_link(but,l))
                links += [link]
            links += [Label(self.Links.frame.interior, text='WEB STREAMS', background='gold', relief=GROOVE)]
            for web in game.web_links:
                link = OldButton(self.Links.frame.interior, text=web, cursor='hand2')
                link.config(command=lambda but=link, l=web: self.open_link(but,l))
                links += [link]
            self.Links.update_buttons(links,'x',2)

        def open_link(self,button,link):
            button.config(highlightbackground='gray')
            if 'acestream://' in link:
                open_soda_player(link)
            else:
                webbrowser.open_new_tab(link)

        def client_exit(self):
            exit()

    root = Tk()
    root.geometry("+10+10")
    root.geometry("%dx%d" % (root.winfo_screenwidth()*.75,root.winfo_screenheight()*.5))
    app = Window(root)

    root.mainloop()

if __name__ == "__main__":
    run()
