# import time
import pyautogui as pag
import os
import numpy as np
import cv2
from mss.darwin import MSS as mss  # If using windows, change to mss.windows
from functools import reduce
import operator
from .positions import get_position_dict

pag.PAUSE = 0.5
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
        self._add_inventory_positions()

    def _shift(self, coord):
        return list(np.add(coord, self.reference))

    def _focus_window(self):
        os.system("open -a firefox")
        pag.move([10, 10])
        pag.move([-10, -10])

    # you may need to use _click_focus() instead of _focus_window()
    def _click_focus(self):
        pag.click(self.reference)

    def _locate_reference(self):
        self._focus_window()
        with mss() as sct:
            filename = sct.shot(mon=-1)

        file = os.path.join(os.path.dirname(__file__), "top_left.png")
        needle = cv2.imread(file, cv2.IMREAD_COLOR)
        needleHeight, needleWidth = needle.shape[:2]
        haystack = cv2.imread(filename, cv2.IMREAD_COLOR)
        result = cv2.matchTemplate(needle, haystack, cv2.TM_CCOEFF_NORMED)
        match_indices = np.arange(result.size)[(result > 0.95).flatten()]
        matches = np.unravel_index(match_indices[:100], result.shape)
        os.remove(filename)
        # you may be off by a factor of 2, so remove the second "/2"
        if len(matches[0]) > 1:
            self.reference = [
                int((np.array(matches[1][0]) + needleWidth / 2) / 2) - 10,
                int((np.array(matches[0][0]) + needleHeight / 2) / 2) - 10,
            ]
        else:
            self.reference = [
                int((matches[1] + needleWidth / 2) / 2) - 10,
                int((matches[0] + needleHeight / 2) / 2) - 10,
            ]
        # self._click_focus()
        # print(self.reference)

    def _search(self, haystack, needle, path=None):
        if path is None:
            path = []
        if needle in haystack:
            path.append(needle)
            return path
        for k, v in haystack.items():
            if isinstance(v, dict):
                result = self._search(v, needle, path + [k])
                if result is not None:
                    return result

    def _getFromDict(self, mapList):
        return reduce(operator.getitem, mapList, self.coords)

    def click(self, x, traverse=False):
        path = self._search(self.coords, x)
        if traverse:
            for i in range(1, len(path)):
                ppath = path[:i]
                pag.click(self._shift(self._getFromDict(ppath)["Button"]))
        pag.click(self._shift(self._getFromDict(path)["Button"]))

    def move(self, x, traverse=False):
        path = self._search(self.coords, x)
        if traverse:
            for i in range(1, len(path)):
                ppath = path[:i]
                pag.click(self._shift(self._getFromDict(ppath)["Button"]))
        pag.moveTo(self._shift(self._getFromDict(path)["Button"]))

    def _add_inventory_positions(self):
        """
        Gets Inventory locations.
        TODO Multiple inventory pages
        """
        x, y = self.coords["Inventory"]["0_0"]["Button"]
        for i in range(6):
            for j in range(13):
                self.coords["Inventory"][f"{i}_{j}"] = {
                    "Button": [x + j * 50, y + i * 50]
                }
