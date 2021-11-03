from tests.base_test import BaseTest
from pages.home_page import HomePage


class TestAccountLogout(BaseTest):
    def test_2c1_account_logout(self):
        page = HomePage(self.driver)
        # page.login()
        page.close_intro()
        page.search_item()
