import geckodriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time

geckodriver_autoinstaller.install()
opts = webdriver.firefox.options.Options()
# opts.set_headless = True # one day headless?
browser = webdriver.Firefox(options=opts)
browser.get("https://www.kongregate.com/games/somethingggg/ngu-idle")
delay = 5  # seconds
try:
    # myElem = WebDriverWait(browser, delay).until(
    #     EC.presence_of_element_located((By.ID, "welcome_username"))
    # )
    # myElemPass = browser.find_element_by_id("welcome_password")
    WebDriverWait(browser, 30).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "gameiframe"))
    )
    file1 = open("MyFile.txt", "a")
    file1.write(browser.page_source)
    file1.close()
    # print(browser.page_source)

    # browser.find_element_by_xpath("//input[@type='text']".send_keys("hi")

    print("Page is ready!")
    browser.switch_to.default_content()

except TimeoutException:
    print("Loading took too much time!")

browser.close()
quit()
# time.sleep(5)
# # get element
# element = driver.find_element_by_id("kong_header_link")
#
# # click the element
# element.click()
