from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .locator import Locator
from .base_page import BasePage


class TrainingGroundPage(BasePage):  # we don't need to call innit cause it inheriting from BasePage where init being
    # called

    url = 'http://techstepacademy.com/training-ground'

    @property
    def button1(self):
        locator = Locator(by=By.ID, value='b1')  # or I can type without "by" and "pass"
        return BaseElement(driver=self.driver, locator=locator)
