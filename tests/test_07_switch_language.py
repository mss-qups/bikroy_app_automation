from tests.base_test import BaseTest
from pages.home_page import HomePage


class TestChangeLangugae(BaseTest):
    def test_01_change_langage(self):
        page = HomePage(self.driver)
        page.login()
        page.switch_language_to_english()
