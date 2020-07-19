from ngubot.game import Game

if __name__ == "__main__":
    game = Game()
    # s = sched.scheduler(time.time, time.sleep)
    # s.enter(3, 1, game.click, ("Sky", True))
    # s.run()

    # game.spend(["ToughnessPlus", "PowerPlus"], "E")
    # game.spend(["TMMPlus"], "M")
    # game.goto("Sky")
    # game.move("RebirthYeah", True)

    game.schedule(1, game.swap, (["NGUAdvA", "TMMPlus"], "L3"))
    game.schedule(1, game.goto, ("HSB",))
    game.schedule(30, game.swap, (["ScissorPlus", "PokePlus"], "L3"), focus=True)
    game.schedule(30, game.goto, ("Sky"))
    print(game.tasks)
    game.run()
