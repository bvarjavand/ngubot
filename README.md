## NGU : Idle BOT

I built this bot while waiting for my game to progress. As the bot started functioning I was afforded more time to work on the bot.  
This is the result.

Currently it works on Mac and Windows, and Linux/GNU.

Ideally you are using Mac/Linus with Firefox.
Otherwise, you have to keep the top left part of the window in the foreground of your desktop/second monitor.

### Installation

clone this directory `git clone https://github.com/bvarjavand/ngubot.git`
cd into it `cd ngubot`
install the package `pip install -e .`

### Setting up
Screenshot the tep-left corner of the game and overwrite `ngl-bot/utils/reference.png`.

### Usage

Look at `examples/big.py` for a small script that clicks on a few things.

Look at `examples/small.py` for a big script which does continuous rebirths, which I used to get to GRB.

The button names are all in `ngubot/utils/positions.xlsx` for reference.

### Acknowledgements
I found a spreadsheet of coordinates from @Zhinjio on discord which I've added to and utilized.

I'll be adding features as I progress through the game.
