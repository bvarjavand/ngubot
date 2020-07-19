from ngubot.utils.base import BaseGame
import pyautogui as pag

import argparse


def explore_dict(game, coords):
    items = coords.items()
    for i in items:
        if i[0] == "Button":
            if len(items) > 1:
                pag.click(game._shift(i[1]))
        else:
            if len(i[1]) > 1:
                explore_dict(game, coords[i[0]])
            else:
                print(i[0])
                print(i[1])
                pag.moveTo(game._shift(i[1]["Button"]))


def main():
    game = BaseGame()
    try:
        for arg in args.search:
            if arg in ["SaveGame", "LoadGame"]:
                pag.moveTo(game._shift(game.coords[arg]["Button"]))
            else:
                pag.click(game._shift(game.coords[arg]["Button"]))
                explore_dict(game, game.coords[arg])
    except KeyError:
        print(f"{args.search} not one of {['All'] + list(game.coords.keys())}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--search",
        nargs="+",
        default=[
            "Rebirth",
            "SpendEXP",
            "SaveGame",
            "LoadGame",
            "Settings",
            "Info",
            "Shop",
            "Basic Training",
            "Fight Boss",
            "Money Pit",
            "Adventure",
            "Inventory",
            "Augmentation",
            "Adv. Training",
            "Time Machine",
            "Blood Magic",
            "Wandoos",
        ],
        help="Menu to test",
    )
    args = parser.parse_args()

    main()
