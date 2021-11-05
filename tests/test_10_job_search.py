from tests.base_test import BaseTest
from pages.home_page import HomePage


class TestJobSearch(BaseTest):
    def test_2c1_job_search(self):
        page = HomePage(self.driver)
        page.close_intro()
        page.click_profile_icon()
        page.switch_language_to_english()
        # page.click_back_eng()
        page.driver.back()
        page.click_home()
        page.click_category_btn()
        page.click_on_jobs()
        page.click_job_search_field()
        page.set_data_on_job_search_field("Python")
        page.click_on_search_btn()
