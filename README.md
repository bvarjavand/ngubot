## NGU : Idle BOT

I built this bot while waiting for my game to progress. As the bot started functioning I was afforded more time to work on the bot.  
This is the result.

Currently it works optimally on a Mac running the game on Kongregate, using Firefox.
Suboptimal performance on a Mac with a different browser, or a Windows on any browser.
There are alternatives for Windows in the #scripting channel in the NGU Discord.

### Installation

Simply clone this directory, and type
`pip install -e .`.

### Setting up
Simply take a screenshot of the tep-left corder of the game and save it as `ngl-bot/utils/reference.png`.

#### I dont have Firefox, or I am using Windows
I've tested this with a friend's windows computer and added comments to `ngubot/utils/base.py` describing what changes need to be made.
You won't 

### Usage

Look at `examples/big.py` for a small script that clicks on a few things.

Look at `examples/small.py` for a big script which does continuous rebirths, which I used to get to GRB.

The button names are all in `ngubot/utils/positions.xlsx` for reference.

### Acknowledgements
I found a spreadsheet of coordinates from @Zhinjio on discord which I've added to and utilized.

I'll be adding features as I progress through the game.
