from tests.base_test import BaseTest
from pages.home_page import HomePage


class TestCheckFavorites(BaseTest):
    def test_2c1_check_favs(self):
        page = HomePage(self.driver)
        page.login()
        page.click_favorite_for_an_ad()