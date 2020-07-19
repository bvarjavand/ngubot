from selenium import webdriver
import geckodriver_autoinstaller

geckodriver_autoinstaller.install()

driver = webdriver.Firefox()
print(driver.command_executor._url)
print(driver.session_id)
