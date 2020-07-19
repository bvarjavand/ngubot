from ngubot.game import Game, run_schedule
import argparse


def main():
    game = Game(locate=True)
    tasks = [
        [1, game.clean, (args.both, args.merge, args.boost, args.trash, args.repeat)]
    ]
    run_schedule(
        tasks, int(args.starttime), int(args.numiters),
    )
    # for some reason it doesn't update game.reference. TODO fix


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o", "--both", nargs="+", default=[], help="Items to merge then boost.",
    )
    parser.add_argument(
        "-m", "--merge", nargs="+", default=[], help="Items to merge.",
    )
    parser.add_argument(
        "-b", "--boost", nargs="+", default=[], help="Items to boost.",
    )
    parser.add_argument(
        "-t", "--trash", nargs="+", default=[], help="Items to trash.",
    )
    parser.add_argument(
        "-r", "--repeat", default=3, help="Number of times to boost each item.",
    )
    parser.add_argument(
        "-s", "--starttime", default=300, help="The time in the run you start."
    )
    parser.add_argument(
        "-n", "--numiters", default=0, help="The time in the run you start."
    )

    args = parser.parse_args()
    main()
