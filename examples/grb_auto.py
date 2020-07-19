from ngubot.game import Game
import argparse

import pyautogui as pag
import sched, time


def main(starttime):
    """
    Needs to be more flexible.
    """
    i = starttime

    def stop():
        pag.press("r")
        pag.press("t")

    game = Game()
    while True:
        s = sched.scheduler(time.time, time.sleep)
        if i < 5:
            s.enter(-starttime + 5, 2, game._locate_reference)
            s.enter(-starttime + 5, 1, game.click, ("Nuke", True))
            s.enter(-starttime + 7, 1, game.clean, (args.both, args.merge, args.boost))

        if i < 20:
            s.enter(-starttime + 20, 2, game._locate_reference)
            s.enter(-starttime + 20, 1, stop)
            s.enter(-starttime + 21, 1, game.click, ("L2", True))
            s.enter(-starttime + 22, 1, game.click, ("Forest", True))
            s.enter(-starttime + 25, 1, game.spend, (["TMEPlus"], "E"))
            s.enter(-starttime + 30, 1, game.spend, (["TackPlus"], "M"))

        if i < 599:
            s.enter(-starttime + 599, 2, game._locate_reference)
            s.enter(
                -starttime + 599, 1, game.clean, (args.both, args.merge, args.boost)
            )
            s.enter(-starttime + 600, 1, stop)
            s.enter(-starttime + 601, 1, game.click, ("L3", True))
            s.enter(-starttime + 610, 1, game.click, ("Sky", True))
            s.enter(-starttime + 612, 1, game.spend, (["TMEPlus"], "E"))
            s.enter(-starttime + 615, 1, game.spend, (["TackPlus"], "M"))

        if i < 900:
            s.enter(-starttime + 900, 2, game._locate_reference)
            s.enter(-starttime + 900, 1, game.spend, (["TackPlus"], "M"))  # MISSED MENU

        if i < 1200:
            s.enter(-starttime + 1200, 2, game._locate_reference)
            s.enter(
                -starttime + 1200, 1, game.clean, (args.both, args.merge, args.boost)
            )

        if i < 1500:
            s.enter(-starttime + 1500, 2, game._locate_reference)
            s.enter(
                -starttime + 1500,
                1,
                game.spend,
                (["ToughnessPlus", "PowerPlus"], "E"),  # Too early
            )

        if i < 1799:
            s.enter(-starttime + 1799, 2, game._locate_reference)
            s.enter(
                -starttime + 1799, 1, game.clean, (args.both, args.merge, args.boost)
            )
            s.enter(-starttime + 1800, 1, game.spend, (["ScissorPlus"], "E"))

        if i < 2250:
            s.enter(-starttime + 2250, 2, game._locate_reference)
            s.enter(-starttime + 2250, 1, stop)
            s.enter(-starttime + 2251, 1, game.click, ("L1", True))
            s.enter(-starttime + 2255, 1, game.spend, (["DangerPlus"], "E"))
            s.enter(-starttime + 2259, 1, game.click, ("Nuke", True))
            s.enter(-starttime + 2260, 3, game.click, ("Right Arrow", True))
            s.enter(-starttime + 2260, 2, game.click, ("Right Arrow", True))
            s.enter(-starttime + 2260, 1, game.click, ("Right Arrow", True))
            s.enter(-starttime + 2265, 1, game.spend, (["AdvACap"], "E"))

        if i < 2380:
            s.enter(-starttime + 2380, 2, game._locate_reference)
            s.enter(-starttime + 2380, 1, game.click, ("Sky", True))
            s.enter(
                -starttime + 2385, 1, game.clean, (args.both, args.merge, args.boost)
            )
        # sky hits the cave

        if i < 3000:
            s.enter(-starttime + 3000, 2, game._locate_reference)
            s.enter(
                -starttime + 3000, 1, game.clean, (args.both, args.merge, args.boost)
            )

        if i < 3500:
            s.enter(-starttime + 3500, 2, game._locate_reference)
            s.enter(-starttime + 3500, 1, game.spend, (["DangerPlus"], "E"))
            s.enter(
                -starttime + 3505, 1, game.clean, (args.both, args.merge, args.boost)
            )
        # inv full
        if i < 3600:
            s.enter(-starttime + 3600, 2, game._locate_reference)
            s.enter(-starttime + 3600, 1, stop)
            s.enter(-starttime + 3601, 1, game.click, ("L1", True))
            s.enter(-starttime + 3602, 1, game.click, ("Nuke", True))

        if i < 3700:
            s.enter(-starttime + 3700, 2, game._locate_reference)
            s.enter(-starttime + 3700, 1, game.click, ("RebirthYeah", True))
        i = 0
        starttime = 0
        s.run()


if __name__ == "__main__":
    items_both = [
        "Head",
        "Chest",
        "Legs",
        "Boots",
        "Weapon",
        "Accessory1",
        "Accessory2",
        "Accessory3",
        "Accessory4",
        "0_0",
        "0_1",
        "1_0",
        "1_1",
        "2_0",
        "2_1",
        "3_0",
        "3_1",
        "3_2",
        "4_0",
        "4_1",
        "4_2",
        "4_3",
        "4_4",
        "4_5",
    ]

    items_merge = [
        "3_3",
        "3_4",
        "3_5",
        "3_6",
        "3_7",
        "3_8",
        "3_9",
    ]

    items_boost = ["3_10", "3_11"]

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o", "--both", nargs="+", default=items_both, help="Menu to test",
    )
    parser.add_argument(
        "-m", "--merge", nargs="+", default=items_merge, help="Menu to test",
    )
    parser.add_argument(
        "-b", "--boost", nargs="+", default=items_boost, help="Menu to test",
    )
    parser.add_argument(
        "-s", "--starttime", default=0, help="The time in the run you start."
    )
    args = parser.parse_args()

    main(int(args.starttime))
