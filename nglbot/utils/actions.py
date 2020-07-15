from .base import BaseGame, click, move
import pyautogui as pag
import time


class Actions(BaseGame):
    def __init__(self, zone, augname, selected):
        """
        Imitializer for the Actions class which scripts can inherit.
        Parameters
        ----------
        zone {Str} : The zone to idle at
        augname {Str} : The augment to power up
        selected {Str} : The items to protect/merge/boost
        """
        super(Actions, self).__init__()
        self.zone = zone
        self.augname = augname  # Currently don't use this
        self.selected = selected

    def locate_reference(self):
        self._locate_reference()
        click(self.reference)

    def fight_boss(self, action):
        if action not in self.bossnames:
            raise ValueError(f"{action} should be one of {self.bossnames}")
        click(self.coords["Menu"]["Fight_Boss"])
        click(self.coords["Fight_Boss"][action])

    def toss_money(self):
        # TODO check
        click(self.coords["Menu"]["Money_Pit"])
        click(self.coords["Money_Pit"]["Toss"])

    def move_to_zone(self):
        try:
            click(self.coords["Menu"]["Adventure"])
            if self.zone == "Itopod":
                self._enter_itopod()
            else:
                click(self.coords["Adventure"]["Dropdown"])
                click(self.coords["Adventure"][self.zone])
        except ValueError:
            print(f"{self.zone} is not in {self.adventurenames}.")

    def increase_zone(self, num=5):
        click(self.coords["Menu"]["Adventure"])
        for _ in range(num):
            pag.press("right")

    def _enter_itopod(self):
        click(self.coords["Adventure"]["Itopod"])
        click(self.coords["Adventure"]["Itopod_Enter"])

    def power_up_selected(self, items, infinity_cube=True):
        if self.items[0] is None:
            if infinity_cube:
                self.items = []
            else:
                return
        for item in self.items:
            if item not in self.coords["Inventory"].keys():
                raise ValueError(f"{item} not one of {self.coords['Inventory'].keys()}")
        click(self.coords["Menu"]["Inventory"])
        for item in self.items:
            move(self.coords["Inventory"][item])
            pag.press("d")
            pag.press("a")
        if infinity_cube:
            pag.click(self.coords["Inventory"]["Infinity_Cube"], button="right")

    def power_up_equipment(self, infinity_cube=False):
        self.power_up_selected(self.inventorynames)

    def trash_unprotected(self):
        click(self.coords["Menu"]["Inventory"])
        pag.keyDown("ctrl")
        for value in self.coords["Inventory"].values():
            click(value)
        pag.keyUp("ctrl")

    def augment(self, augname, change):
        # TODO augnames is a dictionary with amounts
        if augname not in self.augnames:
            raise ValueError(f"{augname} should be one of {self.augnames}")
        changes = ["+", "-"]
        if change not in changes:
            raise ValueError(f"{change} should be one of {changes}")
        click(self.coords["Menu"]["Augmentation"])
        click(self.coords["Augmentation"][augname + "_" + change])

    def basic_train(self):
        click(self.coords["Menu"]["Basic_Training"])
        click(self.coords["Basic_Training"][f"{self.btnames[self.stage]}_Cap"])

    def train(self, augname):
        self.augment(augname, "-")
        self.basic_train()
        self.augment(augname, "+")

    def use_magic(self):
        # TODO more than 1 magic
        click(self.coords["Menu"]["Blood_Magic"])
        click(list(self.coords["Blood_Magic"].values())[0])

    def cast_spell(self, spell):
        click(self.coords["Menu"]["Blood_Magic"])
        click(self.coords["Blood_Magic"]["Cast"])
        try:
            click(self.coords["Blood_Magic"][spell])
            click(self.coords["Blood_Magic"]["Back"])
        except ValueError:
            print(f"{spell} not one of {self.coords['Blood_Magic'].keys()}")

    def rebirth(self, spell="Boost"):
        self.cast_spell(spell)
        click(self.coords["Menu"]["Rebirth"])
        click(self.coords["Rebirth"]["Rebirth"])
        click(self.coords["Rebirth"]["Yes"])
        time.sleep(0.5)
        click(self.coords["Menu"]["Inventory"])
