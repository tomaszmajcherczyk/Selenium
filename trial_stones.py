from selenium.webdriver.common.by import By
from .base_page import BasePage
from .base_element import BaseElement
from .locator import Locator


class TrialPage(BasePage):

    url = 'https://techstepacademy.com/trial-of-the-stones'

    @property
    def stone_input(self):
        locator = Locator(By.ID, 'r1Input')
        return BaseElement(self.driver, locator=locator)

    @property
    def stone_button(self):
        locator = (By.CSS_SELECTOR, 'input#r1Btn')  # other way than By.ID
        return BaseElement(self.driver, locator=locator)

    @property
    def secrets_input(self):
        locator = (By.CSS_SELECTOR, 'input#r2Input')  # other way than By.ID
        return BaseElement(self.driver, locator=locator)

    @property
    def secrets_button(self):
        locator = (By.CSS_SELECTOR, 'input#r2Btn')  # other way than By.ID
        return BaseElement(self.driver, locator=locator)