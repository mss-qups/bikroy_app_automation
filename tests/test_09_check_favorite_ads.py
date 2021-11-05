from tests.base_test import BaseTest
from pages.home_page import HomePage


class TestFavoriteCheck(BaseTest):
    def test_2c1_check_favorite(self):
        page = HomePage(self.driver)
        page.login()
        page.click_favorite_for_an_ad()
        page.click_back()
        page.click_profile_icon()
        page.click_favorites()
