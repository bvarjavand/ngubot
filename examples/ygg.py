# 0 : rb starts
# 10 : nuke
# 15 : swap("TMEPlus", "TMMPlus", "L4"), goto(HSB)
# 60 : seed(FoG)
# 360 : swap("TMEPlus", "TMMPlus", "L3"), nuke
# 3000 : spend(["ToughnessPlus", "PowerPlus"])
# 3600 : swap("ScissorPlus", "PaperPlus")
# kill titans (gold drop loadout)
# scissors/hickey

# state for each menu:
# BT : ignore
# Fight Boss : currBoss
# Money Pit : statusToss, statusSpin
#
#
#
#
#

# def main():
#     game = Game()
#     # s = sched.scheduler(time.time, time.sleep)
#     # s.enter(3, 1, game.click, ("Sky", True))
#     # s.run()

#     # game.spend(["ToughnessPlus", "PowerPlus"], "E")
#     # game.spend(["TMMPlus"], "M")
#     # game.goto("Sky")
#     # game.move("RebirthYeah", True)

#     game.schedule(1, game.swap, (["NGUAdvA", "TMMPlus"], "L3"))
#     game.schedule(1, game.goto, ("HSB",))
#     game.schedule(30, game.swap, (["ScissorPlus", "PokePlus"], "L3"), focus=True)
#     game.schedule(30, game.goto, ("Sky"))
#     print(game.tasks)
#     game.run()
