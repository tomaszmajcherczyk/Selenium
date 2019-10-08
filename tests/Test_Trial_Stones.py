from selenium import webdriver
from pages.trial_page import TrialPage
import time

browser = webdriver.Chrome()

trial_page = TrialPage(driver=browser)
trial_page.go()
trial_page.stone_input.input_text("rock")
trial_page.stone_button.click()

time.sleep(4)
browser.quit()
