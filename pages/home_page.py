import time

from pages.base_page import BasePage
from utils.locators import BikroyLocators
from time import sleep


class HomePage(BasePage):

    def __init__(self, driver):
        self.locator = BikroyLocators
        super().__init__(driver)

    def click_back(self):
        self.click_by_xpath(self.locator.backButton_bang)

    def click_back_eng(self):
        self.click_by_xpath(self.locator.backButton_eng)

    def click_profile_icon(self):
        self.click_by_id(self.locator.profileBtn)

    def click_post_btn(self):
        sleep(3)
        self.click_by_id(self.locator.postBtn)
        time.sleep(3)

    def close_intro(self):
        try:
            sleep(3)
            intro = self.driver.find_element_by_id(self.locator.intro_close_btn)
            sleep(1)
            intro.click()
        except Exception as e:
            print(e)

    def login(self):
        self.close_intro()
        self.click_profile_icon()
        self.click_by_id(self.locator.sign_in_email_btn)
        self.click_by_id(self.locator.emailField)
        self.send_data(self.locator.emailText, self.locator.emailField)
        self.click_by_id(self.locator.passwordField)
        self.send_data(self.locator.passwordText, self.locator.passwordField)
        self.click_by_id(self.locator.loginBtn)
        sleep(1)

    def click_my_ads(self):
        self.click_by_id(self.locator.myAds)

    def click_my_membership(self):
        self.click_by_id(self.locator.myMembership)

    def click_favorites(self):
        self.click_by_id(self.locator.favorites)

    def click_my_profile(self):
        self.click_by_id(self.locator.myProfile)

    def click_search_icon(self):
        self.click_by_id(self.locator.search_icon)

    def click_back_btn(self):
        self.click_by_class_name(self.locator.backButton_bang)

    def search_item(self):
        self.click_search_icon()
        self.click_by_id(self.locator.searchBox)
        sleep(1)
        self.click_by_id(self.locator.editSearchField)
        # self.driver.press_keycode(74)
        self.send_data('Mobile', self.locator.editSearchField)
        sleep(20)
        # self.driver.press_keycode(84)

        # sleep(10)

    def logout(self):
        self.login()
        self.click_by_id(self.locator.logoutBtn)
        time.sleep(2)

    def click_first_product(self):
        sleep(5)
        self.click_by_id(self.locator.first_product)
        sleep(4)

    def tap_settings(self):
        self.click_by_id(self.locator.gear_icon)
        time.sleep(3)

    def tap_english(self):
        self.click_by_xpath(self.locator.english_language)
        sleep(3)

    def switch_language_to_english(self):
        """It will change whole app language to English"""
        self.tap_settings()
        self.tap_english()

    def click_home(self):
        """clicks the home button"""
        self.click_by_id(self.locator.home_btn)

    def click_favorite_icon(self):
        """clicks favorite icon for a item"""
        self.click_by_id(self.locator.favorite_icon)

    def click_favorite_for_an_ad(self):
        """click favorite icon for a item"""
        self.click_home()
        self.click_first_product()
        self.click_favorite_icon()

    def click_category_btn(self):
        """clicks category btn"""
        self.click_by_id(self.locator.category_btn)

    def click_on_jobs(self):
        """clicks jobs"""
        self.click_by_xpath(self.locator.jobs_link)

    def click_job_search_field(self):
        """clicks on job search field"""
        self.click_by_id(self.locator.job_search_field)

    def click_on_search_btn(self):
        """clicks on job search button"""
        self.click_by_id(self.locator.search_btn)

    def set_data_on_job_search_field(self, data):
        """set data on search field"""
        self.send_data(data, self.locator.job_search_field)
