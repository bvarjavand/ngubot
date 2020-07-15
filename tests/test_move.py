from ngubot.utils.base import BaseGame

if __name__ == "__main__":
    game = BaseGame()
    # game.click("Rebirth")
    # game.move("Spin Me", traverse=True)
    # game.move("Nuke", traverse=True)
    # game.click("0_4", traverse=True)
    t = True
    for button in list(game.coords["Fight Boss"].keys())[1:]:
        print("Button", button)
        game.click(button, t)
        t = False
