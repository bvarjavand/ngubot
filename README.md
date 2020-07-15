## NGU : Idle BOT

I built this bot while waiting for my game to progress. As the bot started functioning I was afforded more time to work on the bot.  
This is the result.

Currently it is tested, and works, on Mac and Windows.
It should also work on Linux/GNU but I don't have one of those machines.

Ideally you are using Mac/Linus with Firefox.
Otherwise, you have to keep the top left part of the window in the foreground of your desktop/second monitor.

### Installation

clone this directory, cd into it, and install the package:
```
git clone https://github.com/bvarjavand/ngubot.git
cd ngubot
pip install -e .
```

### Setting up

Screenshot the tep-left corner of the game and overwrite `ngl-bot/utils/reference.png`.

### Usage

Look at `examples/big.py` for a small script that clicks on a few things.

Look at `examples/small.py` for a big script which does continuous rebirths, which I used to get to GRB.

The button names are all in `ngubot/utils/positions.xlsx` for reference.

#### NOTE : FOR NON-FIREFOX USERS

When you initialize a BaseGame object, you must call `BaseGame(firefox=False)`

### Acknowledgements

I found a spreadsheet of coordinates from @Zhinjio on discord which I've added to and utilized.

I'll be adding features as I progress through the game.
