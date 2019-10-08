from selenium import webdriver
from pageobjects.training_ground_page import TrainingGroundPage


browser = webdriver.Chrome()
test_value = 'it worked'

trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == 'Button1'
browser.quit()
