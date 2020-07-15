from utils.actions import Actions
from utils.base import move, click
import argparse
import time


def rebirth_start(game):
    game.fight_boss("nuke")
    game.increase_zone()
    game.time_machine()
    game.use_magic()
    game.augment("Safety_Scissors")


def main():
    game = Actions(args.zone, args.augname, args.selected)
    time.sleep(1)
    game.fight_boss("nuke")


if __name__ == "__main__":
    # todo cumulative selected items, with argparse cumulative
    parser = argparse.ArgumentParser()
    parser.add_argument("--zone", default="Cave_of_Many_Things", help="Zone to idle at")
    parser.add_argument("--selected", default=None, help="Any item positions to boost")
    parser.add_argument(
        "--augname", default="Cannon_Implant", help="Name of an Augment"
    )
    parser.add_argument("start", help="0, 1, 2, 3, 4, 5, 6")
    args = parser.parse_args()
    main()
