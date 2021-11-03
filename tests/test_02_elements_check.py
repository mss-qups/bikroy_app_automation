from tests.base_test import BaseTest
from pages.home_page import HomePage


class TestElementsCheck(BaseTest):
    def test_2c1_elements_check(self):
        account_page = HomePage(self.driver)
        account_page.login()

        # click elements on user profile
        account_page.click_my_ads()
        account_page.click_back_btn()
        account_page.click_my_membership()
        account_page.click_back_btn()
        account_page.click_favorites()
        account_page.click_back_btn()
        account_page.click_my_profile()