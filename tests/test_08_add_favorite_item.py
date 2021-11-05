from tests.base_test import BaseTest
from pages.home_page import HomePage


class TestAddFavorite(BaseTest):
    def test_2c1_add_favorite(self):
        page = HomePage(self.driver)
        page.login()
        page.click_favorite_for_an_ad()
