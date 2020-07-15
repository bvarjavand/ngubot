from utils.actions import Actions
from utils.base import click
import argparse
import time
import pyautogui as pag


class Rebirth(Actions):
    def __init__(self, zone, selected, augname):
        super(Rebirth, self).__init__(zone, augname, selected)
        self.zone = zone
        self.augname = augname
        self.selected = selected

    def _inventory_cycle(self, power_up, trash):
        if power_up:
            self.power_up_equipment()
        self.power_up_selected(self.selected, infinity_cube=True)
        if trash:
            self.trash_unprotected()

    def _train_cycle(self, magic):
        self.train(self.augname)
        if magic:
            self.use_magic()

    def cycle(self, magic=True, power_up=False, trash=False):
        self._train_cycle(magic=magic)
        self._inventory_cycle(power_up=power_up, trash=trash)

    def start_rebirth(self, itopod=False, trash=False):
        self.basic_train()
        time.sleep(1)
        self.fight_boss("Nuke")
        time.sleep(3)
        self.increase_zone(5)
        self.augment(self.augname, "+")
        self.use_magic()
        self._inventory_cycle(power_up=False, trash=trash)

    def end_rebirth(self):
        self.fight_boss("Nuke")
        time.sleep(1)
        self.rebirth()

    def rebirth_cycle(self, t, locate):
        self.stage = t
        if locate:
            self.locate_reference()
        else:
            self._focus_window()
            time.sleep(1)
        if t == 0:
            self.start_rebirth(itopod=False, trash=False)
        if t == 1:
            self.move_to_zone(self.zone)
        if t in [1, 2, 3, 4, 5]:
            self.cycle()
        if t == 6:
            self.end_rebirth()


def loop(game, state, initial_pos=None, locate=True):
    if initial_pos is None:
        initial_pos = pag.position()
    state_wait = {0: 100, 1: 200, 2: 300, 3: 400, 4: 500, 5: 600, 6: 1}
    game.rebirth_cycle(state, locate)
    click(initial_pos)
    time.sleep(state_wait[state])
    state = (state + 1) % 7
    loop(game, state, locate=locate)


def main():
    initial_pos = pag.position()
    game = Rebirth(args.zone, [args.selected], args.augname)
    state = int(args.start)
    loop(game, state, initial_pos, locate=False)


if __name__ == "__main__":
    # todo cumulative selected items, with argparse cumulative
    parser = argparse.ArgumentParser()
    parser.add_argument("--zone", default="Cave_of_Many_Things", help="Zone to idle at")
    parser.add_argument("--selected", default=None, help="Any item positions to boost")
    parser.add_argument(
        "--augname", default="Cannon_Implant", help="Name of an Augment"
    )
    parser.add_argument("start", help="0, 1, 2, 3, 4, 5, 6")
    args = parser.parse_args()
    main()
