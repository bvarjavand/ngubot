# import geckodriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import geckodriver_autoinstaller


class DriverSession:
    def __init__(self):
        geckodriver_autoinstaller.install()
        options = Options()
        # options.headless = True
        self.driver = webdriver.Firefox(options=options)
        self.driver.get("https://www.kongregate.com/games/somethingggg/ngu-idle")
        print("Press enter once the game is loaded to continue:")
        input()
        self.gameid = self.driver.find_element_by_id("gameiframe")

    def _click(self, pos, traverse=True, right=False):
        """
        pos : tuple
            The coordinates to click, in order. ex: ([30, 50],)
        right : bool
            Whether to right click
        """
        if type(pos) is str:
            pos = (pos,)
        actions = ActionChains(self.driver)
        if not traverse:
            pos = (pos[-1],)
        for p in pos:
            actions.move_to_element_with_offset(self.gameid, p[0], p[1])
            if right:
                actions.context_click()
            else:
                actions.click()
        actions.perform()

    def click(self, pos, traverse=True, right=False):
        self.driver.refresh()
        WebDriverWait(self.driver, 30).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "gameiframe"))
        )
        browser.switch_to.default_content()
        self.gameid = self.driver.find_element_by_id("gameiframe")
        print(self.gameid.location)
        print(pos)
        self._click(pos, traverse, right)

    def _press(self, keys, pos, traverse=True):
        """
        keys : tuple
            The keys to click, in order, at each pos. ex: ("d", "a")
        pos : tuple
            The coordinates to press keys at, in order. ex: ([30, 50],)
        right : bool
            Whether to right click
        """
        if type(pos) is str:
            pos = (pos,)
        if type(keys) is str:
            keys = (keys,)
        actions = ActionChains(self.driver)
        if not traverse:
            pos = (pos[-1],)
        for p in pos:
            actions.move_to_element_with_offset(self.gameid, p[0], p[1])
            for key in keys:
                actions.send_keys(key)
        actions.perform()

    def press(self, keys, pos, traverse=True):
        try:
            self.gameid = self.driver.find_element_by_id("gameiframe")
            self._press(keys, pos, traverse)
        except StaleElementReferenceException:
            self.gameid = self.driver.find_element_by_id("gameiframe")
            self._press(keys, pos, traverse)
