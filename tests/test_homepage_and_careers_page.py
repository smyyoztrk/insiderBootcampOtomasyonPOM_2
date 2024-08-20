import pytest
import softest
from time import sleep
from pages.home_page import HomePage
from pages.careers_page import CareersPage

@pytest.mark.usefixtures("setUp")
class TestHomepageAndCareersPage(softest.TestCase):
    def test_home_page_is_loaded(self):
        homepage = HomePage(self.driver)
        homepage.load()
        assert homepage.is_loaded(), "Insider home page is not loaded"
        
    def test_careers_page_is_loaded(self):
        homepage = HomePage(self.driver)
        careerspage = CareersPage(self.driver)
        homepage.load()
        homepage.click_menu_item(homepage.COMPANY_MENU)
        homepage.go_to_careers()
        assert careerspage.is_careers_page_loaded(), "Careers home page is not loaded"
        # assert careerspage.is_teams_block_displayed(), "Teams block page is not loaded"
        self.soft_assert(self.assertTrue, careerspage.is_teams_block_displayed(), "Teams block page is not loaded")
        # assert careerspage.is_locations_block_displayed(), "Locations block is not loaded"
        self.soft_assert(self.assertTrue, careerspage.is_locations_block_displayed(), "Locations block is not loaded")
        # assert careerspage.is_insiderat_life_block_displayed(), "Insider At Life block is not loaded"
        self.soft_assert(self.assertTrue, careerspage.is_insiderat_life_block_displayed(), "Insider At Life block is not loaded")
        self.assert_all()