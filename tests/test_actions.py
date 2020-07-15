from ngl_runner.utils.actions import Actions
from ngl_runner.utils.base import click, move


def test_action(game):
    click()
    move()


def main():
    game = Actions()
    test_action(game)


if __name__ == "__main__":
    main()
