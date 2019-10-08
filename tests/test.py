from selenium import webdriver
import time
browser = webdriver.Chrome()
from selenium.webdriver.common.by import By

browser.get("https://the-internet.herokuapp.com/add_remove_elements/")
button1_loc = 'button'
# button4_xpath_locator = "//button[@id='b4']"

# Assign elements
input2_elem = browser.find_element(button1_loc)
# button4_elem = browser.find_element_by_xpath(button4_xpath_locator)


# Manipulate elements
# input2_elem.send_keys("Test")
# button4_elem.click()
input2_elem.click()

time.sleep(5)
browser.quit()

# need to be careful when writing code I wrote down line 7 button with one t and it just get to the page, it didn't
# even found css_locator and there is no indication here in pycharm.
