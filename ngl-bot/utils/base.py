import time
import pyautogui as pag
import os
import numpy as np
import cv2
from mss.darwin import MSS as mss

if __name__ == "__main__":
    from positions import get_position_dict
else:
    from .positions import get_position_dict

# pag.PAUSE = 0.25
pag.PAUSE = 0.25
pag.FAILSAFE = True


class BaseGame:
    """
    Base class whenever a macro session starts.
    Instantiates all button locations in the form
    self.coords[<menu_title>][<button_name>] (self.coords["Inventory"]["Helm"])

    Most pressing TODO's are Adventure Attack Buttons and Blood Magic Buttons
    """

    def __init__(self):
        self._locate_reference()
        _, _, self.coords = get_position_dict()

    def _shift(self, coord):
        return list(np.add(coord, self.reference))

    def _focus_window(self):
        os.system("open -a firefox")

    def _locate_reference(self):
        self._focus_window()
        time.sleep(2)
        with mss() as sct:
            filename = sct.shot(mon=-1)

        file = os.path.join(os.path.dirname(__file__), "top_left.png")
        needle = cv2.imread(file, cv2.IMREAD_COLOR)
        needleHeight, needleWidth = needle.shape[:2]
        haystack = cv2.imread(filename, cv2.IMREAD_COLOR)
        result = cv2.matchTemplate(needle, haystack, cv2.TM_CCOEFF_NORMED)
        match_indices = np.arange(result.size)[(result > 0.95).flatten()]
        matches = np.unravel_index(match_indices[:100], result.shape)
        # BUG when on rebirth screen, how to handle multiple matches
        os.remove(filename)
        self.reference = [
            int((matches[1] + needleWidth / 2) / 2) - 10,
            int((matches[0] + needleHeight / 2) / 2) - 10,
        ]

    def _getpath(self, value, prepath=()):
        for k, v in self.coords.items():
            path = prepath + (k,)
            if k == value:  # found value
                return path
            elif hasattr(v, "items"):  # v is a dict
                p = getpath(v, value, path)  # recursive call
                if p is not None:
                    return p

    def click(x, traverse=False):
        path = self._getpath(x)
        coord = self.coords
        if traverse:
            for item in path[:-1]:
                pag.click(coord[item]["Button"])
                coord = coord[iten]
        pag.click(coord[path[-1]]["Button"])

    def move(x, traverse=False):
        path = self._getpath(x)
        coord = self.coords
        if traverse:
            for item in path[:-1]:
                pag.click(coord[item]["Button"])
                coord = coord[iten]
        pag.moveTo(coord[path[-1]]["Button"])

    def _get_rebirth_locs(self):
        """
        Gets rebirth button locations.
        TODO difficulty and checking "Crap_To_Do"
        """
        self.coords["Rebirth"] = {}
        self.coords["Rebirth"]["Rebirth"] = list(
            np.array([540, 510]) + np.array(self.reference)
        )
        self.coords["Rebirth"]["Yes"] = list(
            np.array([430, 305]) + np.array(self.reference)
        )
        self.coords["Rebirth"]["No"] = list(
            np.array([500, 305]) + np.array(self.reference)
        )

    def _get_inventory_locs(self):
        """
        Gets Inventory locations.
        TODO Multiple inventory pages
        """
        self.coords["Inventory"] = {}
        equip_grid = np.array(
            [
                [
                    np.array([465, 50])
                    + np.array(self.reference)
                    + np.array([50 * i, 50 * j])
                    for i in range(4)
                ]
                for j in range(4)
            ]
        )
        matching_inds = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (1, 2), (1, 3)]
        for i in range(len(matching_inds)):
            self.coords["Inventory"][self.inventorynames[i]] = list(
                equip_grid[matching_inds[i]]
            )
        inventory_grid = np.array(
            [
                [
                    np.array([340, 320])
                    + np.array(self.reference)
                    + np.array([50 * i, 50 * j])
                    for i in range(12)
                ]
                for j in range(4)
            ]
        )
        for i in range(4):
            if i < 3:
                for j in range(12):
                    self.coords["Inventory"][f"{i}_{j}"] = list(inventory_grid[i, j])
            else:  # I dont have all the slots yet
                for j in range(6):
                    self.coords["Inventory"][f"{i}_{j}"] = list(inventory_grid[i, j])
