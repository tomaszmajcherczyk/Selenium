from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(object):

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None  # none because we need to find it first
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))  # locator
        # basically means a tuple like this one on the line 15
        self.web_element = element  # we populate
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    @property
    def text(self):
        text = self.web_element.text
        return text

