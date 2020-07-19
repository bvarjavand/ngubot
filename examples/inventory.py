from ngubot.game import Game
import argparse

items_both = []

items_merge = ["4_4", "4_8", "4_9", "4_10", "4_11", "4_12", "5_5", "5_6"]

items_boost = ["4_12", "Head", "Chest", "5_10", "4_11"]


def main():
    if int(args.numiters) == 0:
        iter = 1
        while True:
            game = Game(locate=False)
            game.schedule(
                int(args.interval), game.clean, (args.both, args.merge, args.boost)
            )
            game.run(int(args.starttime))
            print("Iteration", iter)
            iter += 1
    else:
        for iter in range(1, int(args.numiters) + 1):
            game = Game(locate=False)
            game.schedule(
                int(args.interval), game.clean, (args.both, args.merge, args.boost)
            )
            game.run(int(args.starttime))
            print("Iteration", iter)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o",
        "--both",
        nargs="+",
        default=items_both,
        help="Items to merge then boost.",
    )
    parser.add_argument(
        "-m", "--merge", nargs="+", default=items_merge, help="Items to merge.",
    )
    parser.add_argument(
        "-b", "--boost", nargs="+", default=items_boost, help="Items to boost.",
    )
    parser.add_argument(
        "-r", "--repeat", default=3, help="Number of times to boost each item.",
    )
    parser.add_argument(
        "-s", "--starttime", default=0, help="The time in the run you start."
    )
    parser.add_argument(
        "-i",
        "--interval",
        default=300,
        help="How often to execute the command (-starttime).",
    )
    parser.add_argument(
        "-n", "--numiters", default=0, help="The time in the run you start."
    )

    args = parser.parse_args()

    main()
