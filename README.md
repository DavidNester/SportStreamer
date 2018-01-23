#     SportStreamer

Application used to mine streaming links for various sports from reddit forums designated for
posting stream links. I use Beautiful Soup to parse the pages and get the links. This uses
acestreams and opens them automatically in [SodaPlayer](https://www.sodaplayer.com/). It also
gives links to web streams and will open them as a new tab in your browser.

- GUImain.py -- main file to run. Runs GUI
- Utility.py -- contains a few functions, global variables, and import statements
- Forum.py -- Class for a reddit streaming forum like [Soccer Streams](https://www.reddit.com/r/soccerstreams/)
- Game.py -- Class for a game (also a post in a forum)
- Column.py -- Stores list of buttons and wrapper for scrollable frame
- scrframe -- Scrollable frame class found on stackoverflow
- OLD -- Files that I no longer use. Command line interface and more basic GUI version

This works on my 2013 Macbook Pro with HighSierra 10.13.2. Have not tested on other platforms or OS versions.

# Things I Intend To Do
- Compile into app so that script doesn't have to be run every time
- Get game data
- Directly to chromecast
- GUI improvements

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
Some mac users may have to use "python3 GUImain.py"
