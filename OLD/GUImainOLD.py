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
#from Column import Column

# TODO: Get game data
# TODO: Make links frame scrollable
# TODO: Add button to class?
# TODO: Use Reddit API?
# TODO: Chromecast --> https://github.com/balloob/pychromecast
# TODO: Handle improper characters


def onFrameConfigure(canvas):
    """Reset the scroll region to encompass the inner frame"""
    canvas.configure(scrollregion=canvas.bbox("all"))


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
            #self.game_canvas = Canvas(self.master, borderwidth=0, background="#ffffff")
            #self.link_canvas = Canvas(self.master, borderwidth=0, background="#ffffff")
            self.sport_frame = Frame(self.master, bg='SeaGreen3',relief=GROOVE)
            self.sport_frame.pack(fill='y', side=LEFT)
            self.game_frame = Frame(self.master, bg='SkyBlue3')
            self.game_frame.pack(fill='y', side=LEFT)
            self.link_frame = Frame(self.master, bg='forest green')
            self.link_frame.pack(fill='y', side=LEFT)
            """
            self.game_vsb = Scrollbar(self.master, orient="vertical", command=self.game_canvas.yview)
            self.link_vsb = Scrollbar(self.master, orient="vertical", command=self.link_canvas.yview)
            self.game_canvas.configure(yscrollcommand=self.game_vsb.set)
            self.link_canvas.configure(yscrollcommand=self.link_vsb.set)
            self.game_vsb.pack(side="right", fill="y")
            self.link_vsb.pack(side="right", fill="y")
            self.game_canvas.pack(side="left", fill="both", expand=True)
            self.game_canvas.create_window((4, 4), window=self.game_frame, anchor="nw")
            self.link_canvas.pack(side="left", fill="both", expand=True)
            self.link_canvas.create_window((4, 4), window=self.link_frame, anchor="nw")
            self.game_frame.bind("<Configure>", lambda event, canvas=self.game_canvas: onFrameConfigure(canvas))
            self.link_frame.bind("<Configure>", lambda event, canvas=self.link_canvas: onFrameConfigure(canvas))
            """
            self.make_sport_buttons()


        def make_sport_buttons(self):
            for sport in SPORTS:
                button = Button(self.sport_frame, text=sport, padx=2, pady=10)
                button.config(command=lambda address=SPORTS[sport], but=button: self.sport_click(but,address))
                if self.forum is None:
                    temp_button = button
                    self.forum=Forum(SPORTS['Soccer'])
                button.pack(fill='x',pady=10)
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
            self.game_frame = Frame(self.master, bg='SkyBlue3',pady=5)
            self.game_frame.pack(fill='y', side=LEFT)
            self.links = []
            self.link_frame = Frame(self.master, bg='forest green',padx=5)
            self.link_frame.pack(fill='y', side=LEFT)
            for game in self.forum.games:
                temp_button = Button(self.game_frame, text=game.text, pady=5)
                temp_button.config(command=lambda g=game, but=temp_button: self.game_click(g, but))
                self.game_buttons += [temp_button]
            self.draw()

        def game_click(self, game, button):
            # grey out current button and reset old button
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
            self.links += [Label(self.link_frame, text='ACESTREAMS', relief=GROOVE)]
            for ace in game.ace_links:
                link = Button(self.link_frame, text=ace, fg='blue', cursor='hand2', pady=2)
                link.config(command=lambda but=link,l=clean_ace(ace): self.open_link(but,l))
                self.links += [link]
            self.links += [Label(self.link_frame, text='WEB STREAMS', relief=GROOVE)]
            for web in game.web_links:
                link = Button(self.link_frame, text=web, fg='blue', cursor='hand2', pady=2)
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
                button.pack(pady=5)
            # draw links
            for link in self.links:
                link.pack(pady=2)

        def client_exit(self):
            exit()

    root = Tk()
    root.geometry("1200x800")
    app = Window(root)

    root.mainloop()

if __name__ == "__main__":
    run()
