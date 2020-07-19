from .utils.base import BaseGame
from .driver import DriverSession
import sched, time


class Bot(BaseGame):
    def __init__(self):
        super().__init__(False, False)
        self.driver = DriverSession()
        self.tasks = []
        self.s = sched.scheduler(time.time, time.sleep)

    def click_path(self, v, traverse=True, right=False):
        path = self._search_value(self.coords, v)
        print(path)
        self.driver.click(path, traverse, right)

    def press_path(self, k, v, traverse=True):
        path = self._search_value(self.coords, v)
        self.driver.press(k, path, traverse)

    def clean(self, itemsToBoth, itemsToMerge, itemsToBoost, repeat=1):
        """
        Cleans the inventory, its basically a customizable automerge/boost.
        """
        traverse = True
        for item in itemsToBoth:
            self.driver.press_path("d", item, traverse)
            self.driver.press_path("a", item, traverse)
            traverse = False
        for item in itemsToMerge:
            self.driver.press_path("d", item, traverse)
            traverse = False
        for item in itemsToBoost:
            self.driver.press("a", item, traverse)
            traverse = False
        self.move("InfCube", False)
        self.click_path(
            self.coords["Inventory"]["InfCube"]["Button"], right=True,
        )

    def _stop_spend(self, type="E"):
        if type == "E":
            self.driver.press_path("r")
        elif type == "M":
            self.driver.press_path("t")

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
                self.click_path(f"{typ}CapCap", True)
            elif len(dests) == 2:
                self.click_path(f"{typ}CapHalf", True)
            else:
                raise ValueError(f"{dests} should be of length 1 or 2!")
            self._stop_spend(typ)
            for dest in dests:
                self.click_path(dest, True)

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
            self.click_path(loadout, True)
        except KeyError:
            keys = [i for i in list(self.coords["Inventory"].keys()) if "L" in i]
            print(f"{loadout} is not in {keys}")
        self.spend(destss)

    def goto(self, dest):
        """
        Travels to a map
        """
        if dest in ["Safe", "Tutorial", "Sewers", "Forest", "Cave", "Sky", "HSB"]:
            self.click_path(dest, True)
        else:
            # self.driver.scroll(10)
            pass

    def schedule(self, t, method, args=()):
        prio = 1
        sametime = [task for task in self.tasks if task[0] == t]
        if len(sametime) == 0:
            self.tasks.append([t, 1, self._locate_reference, ()])
        for task in sametime[::-1]:
            task[1] += prio
            prio += 1
        self.tasks.append([t, 1, method, args])

    def run(self):
        print(self.tasks)
        for item in self.tasks:
            self.s.enter(*item)
        self.s.run()

    def quit(self):
        self.driver.driver.close()
        self.driver.driver.quit()


def run_schedule(tasks, start, num_iters=0, starttime=0):
    """
    Runs a schedule, given a list of tasks of the form :
    tasks = [[time1, method1, args1], [time2, method2, args2]]
    """
    if num_iters == 0:
        iter = 1
        while True:
            game = Game(locate=False)
            for task in tasks:
                task[0] += start
                game.schedule(*task)
            game.run()
            print("Iteration", iter, "\n", time.time)
            iter += 1
    else:
        for iter in range(1, int(args.numiters) + 1):
            game = Game(locate=False)
            for task in tasks:
                game.schedule(*task)
            game.run()
            print("Iteration", iter, "\n", time.time)
