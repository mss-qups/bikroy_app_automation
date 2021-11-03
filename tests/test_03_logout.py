from tests.base_test import BaseTest
from pages.home_page import HomePage


class TestAccountLogout(BaseTest):
    def test_2c1_account_logout(self):
        account_page = HomePage(self.driver)
        account_page.logout()