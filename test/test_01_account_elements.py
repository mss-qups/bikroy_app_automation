from test.base_test import BaseTest
from pages.home_page import HomePage


class TestAccountElems(BaseTest):
    def test_01_account_element(self):
        pass
        home_page = HomePage(self.driver)
        home_page.click_profile_icon()