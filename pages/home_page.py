from pages.base_page import BasePage
from utils.locators import BikroyLocators


class HomePage(BasePage):

    def __init__(self, driver):
        self.locator = BikroyLocators
        super().__init__(driver)

    def click_profile_icon(self):
        self.click(*self.locator.profileBtn)