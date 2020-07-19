from ngubot.bot import Bot
import time
import argparse


def main():
    if args.new:
        bot = Bot()
    else:
        time.sleep(5)
    bot.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--new", default=True)
    args = parser.parse_args()
    main()
