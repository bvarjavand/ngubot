from nglbot.utils.base import BaseGame
import pyautogui as pag
import time

game = BaseGame()


def clean(game):
    itemsToMerge = [
        "Head",
        "Chest",
        "Legs",
        "Boots",
        "Weapon",
        "Accessory1",
        "0_0",
        "0_1",
        "0_2",
        "0_3",
        "0_4",
        "0_5",
        "0_6",
        "0_7",
    ]
    itemsToBoost = [
        "Head",
        "Chest",
        "Legs",
        "Boots",
        "Weapon",
        "Accessory1",
        "0_0",
        "0_1",
        "0_2",
        "0_6",
        "3_9",
    ]
    path = True
    for item in itemsToMerge:
        game.move(item, path)
        pag.press("d")
        path = False
    for item in itemsToBoost:
        game.move(item, path)
        pag.press("a")
    game.move("InfCube", False)
    pag.click(
        game._shift(game.coords["Inventory"]["InfCube"]["Button"]), button="right"
    )


while True:
    # 0, 0
    game.click("Feed Me", True)
    game.click("Really", True)
    game.click("RebirthYeah", False)

    time.sleep(1)
    game.click("IdleAttackPlus", True)

    clean(game)

    game.click("Nuke", True)
    game.click("Right Arrow", True)
    for _ in range(4):
        game.click("Right Arrow", False)

    game.click("ShoulderPlus", True)
    game.click("TackPlus", True)

    time.sleep(300)
    # 330, 5.5
    game._focus_window()

    clean(game)
    game.click("ShoulderPlus", True)
    game.click("TackPlus", True)

    time.sleep(300)
    # 750, 12.5
    game._focus_window()

    clean(game)

    game.click("Nuke", True)
    game.click("Left Arrow", True)
    for _ in range(6):
        game.click("Left Arrow", False)
    for _ in range(6):
        game.click("Right Arrow", False)

    pag.press("r")
    game.click("TMEPlus", True)
    game.click("TackPlus", True)

    time.sleep(300)
    # 1100, 18.3
    game._focus_window()

    clean(game)

    time.sleep(300)
    # 1420, 23.6
    game._focus_window()

    clean(game)

    game.click("Nuke", True)
    game.click("Left Arrow", True)
    for _ in range(6):
        game.click("Left Arrow", False)
    for _ in range(6):
        game.click("Right Arrow", False)

    pag.press("r")
    game.click("ShoulderPlus", True)
    game.click("TackPlus", True)

    time.sleep(300)
    # 1750, 29.1 (adv training unlocked)
    game._focus_window()

    clean(game)

    pag.press("r")
    game.click("PowerPlus", True)
    pag.press("t")
    game.click("CutsPlus")

    time.sleep(240)
    # ~ 2000, 33.3
    game._focus_window()

    clean(game)

    game.click("Feed Me", True)
    game.click("Really", True)
    game.click("RebirthYeah", False)

    time.sleep(1)
