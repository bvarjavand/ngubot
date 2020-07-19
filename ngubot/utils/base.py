import pyautogui as pag
import os
import numpy as np
import cv2
from functools import reduce
import operator
from .positions import get_position_dict
import platform

system = platform.system()
if system == "Darwin":
    from mss.darwin import MSS as mss  # MacOS X
elif system == "Windows":
    from mss.windows import MSS as mss  # Microsoft Windows
elif system == "Linux":
    from mss.linux import MSS as mss  # GNU/Linux
else:
    raise OSError(f"You are using {system}, an os I wasn't expecting. Let me know.")


pag.PAUSE = 0.2
pag.FAILSAFE = True


class BaseGame:
    """
    Base class whenever a macro session starts.
    Instantiates all button locations in the form
    self.coords[<menu_title>][<button_name>] (self.coords["Inventory"]["Helm"])

    Most pressing TODO's are Adventure Attack Buttons and Blood Magic Buttons
    """

    def __init__(self, firefox=True, locate=True):
        self.mac = system == "Darwin"
        self.firefox = firefox
        self.reference = [0, 0]
        if locate:
            self._locate_reference()
        _, _, self.coords = get_position_dict()

    def _shift(self, coord):
        return list(np.add(coord, self.reference))

    def _focus_window(self):
        os.system("open -a firefox")
        pag.move([10, 10])
        pag.move([-10, -10])

    def _click_focus(self):
        pag.click(self.reference)

    def _locate_reference(self):
        if self.firefox:
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

        if len(matches[0]) > 1:  # multiple matches, we take the first one
            matchx = np.array(matches[1][0]) + needleWidth / 2
            matchy = np.array(matches[0][0]) + needleHeight / 2
        else:
            matchx = np.array(matches[1]) + needleWidth / 2
            matchy = np.array(matches[0]) + needleHeight / 2
        if self.mac:  # double resolution for some reason
            matchx /= 2
            matchy /= 2
        self.reference = [
            int(matchx) - 10,
            int(matchy) - 10,
        ]
        if not self.firefox:
            self._click_focus()
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

    def _search_value(self, haystack, needle, path=None):
        if path is None:
            path = []
        if needle in haystack:
            path.append(haystack[needle]["Button"])
            return path
        for k, v in haystack.items():
            if isinstance(v, dict):
                result = self._search_value(v, needle, path + [v["Button"]])
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
