from .utils.base import BaseGame
import pyautogui as pag
import sched, time


class Game(BaseGame):
    def __init__(self, locate=True):
        self.locate = locate
        super().__init__(self, self.locate)
        self.tasks = []
        self.s = sched.scheduler(time.time, time.sleep)

    def clean(self, itemsToBoth, itemsToMerge, itemsToBoost, itemsToTrash=[], repeat=1):
        """
        Cleans the inventory, its basically a customizable automerge/boost.
        """
        path = True
        for item in itemsToBoth:
            self.move(item, path)
            pag.press("d")
            for _ in range(int(repeat)):
                pag.press("a")
            path = False
        for item in itemsToMerge:
            self.move(item, path)
            pag.press("d")
            path = False
        for item in itemsToBoost:
            self.move(item, path)
            for _ in range(int(repeat)):
                pag.press("a")
            path = False
        pag.keyDown("ctrl")
        for item in itemsToTrash:
            self.click(item, path)
            path = False
        pag.keyUp("ctrl")
        self.move("InfCube", False)
        pag.click(
            self._shift(self.coords["Inventory"]["InfCube"]["Button"]), button="right",
        )

    def _stop_spend(self, type="E"):
        if type == "E":
            pag.press("r")
        elif type == "M":
            pag.press("t")

    def _check_resource(self, ds):
        for t in ["E", "M", "R3"]:
            if (
                any([f"{t}Plus" in d for d in ds])
                or any([f"{t}Minus" in d for d in ds])
                or any([f"{t}Cap" in d for d in ds])
            ):
                return t
        for d in ds:
            path = self._search(self.coords, d)
            if "Blood Magic" in path:
                return "M"
            elif (
                "Basic Training" in path
                or "Augmentation" in path
                or "Adv. Training" in path
                or "Energy" in path
            ):
                return "E"
        raise KeyError(f"I didn't expect to get {ds}.")

    def spend(self, destss, swap=None):
        if type(destss) is not list and type(destss) is not tuple:
            destss = [destss]
        for dests in destss:
            if type(dests) is not list:
                dests = [dests]
            typ = self._check_resource(dests)
            print(dests)
            if len(dests) == 1:
                self.click(f"{typ}CapCap", True)
            elif len(dests) == 2:
                self.click(f"{typ}CapHalf", True)
            else:
                raise ValueError(f"{dests} should be of length 1 or 2!")
            self._stop_spend(typ)
            for dest in dests:
                self.click(dest, True)

    def swap(self, destss, loadout):
        typ_E = False
        typ_M = False
        for dests in destss:
            if type(dests) is not list:
                dests = [dests]
            print(dests)
            typ = self._check_resource(dests)
            if typ == "E":
                typ_E = True
            if typ == "M":
                typ_M = True
        if not typ_E and typ_M:
            raise ValueError(f"Need Energy and Magic destinations, not {dests}")
        self._stop_spend("E")
        self._stop_spend("M")
        try:
            self.click(loadout, True)
        except KeyError:
            keys = [i for i in list(self.coords["Inventory"].keys()) if "L" in i]
            print(f"{loadout} is not in {keys}")
        self.spend(destss)

    def goto(self, dest):
        """
        Travels to a map
        """
        if dest in ["Safe", "Tutorial", "Sewers", "Forest", "Cave", "Sky", "HSB"]:
            self.click(dest, True)
        else:
            # pag.scroll(10)
            pass

    def schedule(self, t, method, args=()):
        # TODO handle multiple tasks at the same time.
        # prio = 1
        # sametime = [task for task in self.tasks if task[0] == t]
        # if len(sametime) == 0:
        #     self.tasks.append([t, 1, self._locate_reference, ()])
        # for i in range(len(sametime), 1, -1):
        #     self.tasks
        # for task in sametime[::-1]:
        #     task[1] += prio
        #     prio += 1
        self.tasks.append([t, 1, self._locate_reference, ()])
        self.tasks.append([t, 2, method, args])

    def run(self):
        print(self.tasks)
        for item in self.tasks:
            self.s.enter(*item)
        self.s.run()


def run_schedule(tasks, start, num_iters=0, starttime=0):
    """
    Runs a schedule, given a list of tasks of the form :
    tasks = [[time1, method1, args1], [time2, method2, args2]]
    """
    if int(num_iters) == 0:
        iter = 1
        while True:
            game = Game(locate=False)
            for task in tasks:
                # task[0] += start
                game.schedule(task[0] + int(start), *task[1:])
            game.run()
            print("Iteration", iter, "\n", time.time)
            iter += 1
    else:
        for iter in range(1, int(num_iters) + 1):
            game = Game(locate=False)
            for task in tasks:
                game.schedule(task[0] + int(start), *task[1:])
            game.run()
            print("Iteration", iter, "\n", time.time)
