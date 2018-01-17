#     SportsStreamer

Application used to mine streaming links for various sports from reddit forums designated for
posting stream links. I use Beautiful Soup to parse the pages and get the links. This uses
acestreams and opens them automatically in [SodaPlayer](https://www.sodaplayer.com/). It also
gives links to web streams and will open them as a new tab in your browser.

- GUImain.py -- main file to run. Runs GUI
- Utility.py -- contains a few functions, global variables, and import statements
- Forum.py -- Class for a reddit streaming forum like [Soccer Streams](https://www.reddit.com/r/soccerstreams/)
- Game.py -- Class for a game (also a post in a forum)
- CommandLineMain.py -- initial version with a command line interface. most basic functionality.

This project is still in *early development stages* so there are many features to add, bugs to
fix, and lots cleaning to be done. It is now at a stage where it is functional for me in my
needs. It still requires some technical knowledge to use but I am hoping to get it to a point
where anyone could download and use it.

Please feel free to add to it or suggest updates. I am using this as a learning experience
and am adding things as I discover them. I am sure I am doing many things in bad ways -- some I
am aware of and intend to fix and others I am unaware of a better way to do them. Any advice,
suggestions, and improvements are welcomed.

#     To Use
Uses [Python 3.6.2](https://www.python.org/downloads/release/python-362/)
Install with [pip](https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py) 
```
cd location/to/save/project/in/
mkdir SportStreamer
cd SportStreamer
git init
git clone https://github.com/DavidNester/SportStreamer.git
cd SportStreamer
pip install -r requirements.txt
python GUImain.py 
```

I apologize for the horrible GUI...
