from tests.base_test import BaseTest
from pages.home_page import HomePage


class TestAccountLogin(BaseTest):
    def test_01_account_login(self):
        home_page = HomePage(self.driver)
        home_page.login()