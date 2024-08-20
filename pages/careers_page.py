from selenium.webdriver.common.by import By
from pages.page_base import Pagebase


class CareersPage(Pagebase):
    LIFEATINSİDER_BLOCK = (By.XPATH,"//h2[contains (text(), 'Life at Insider')]")
    LOCATIONS_BLOCK = (By.XPATH,"//h3[contains (text(), 'Our Locations ')]")  
    TEAMS_BLOCK = (By.XPATH,"//h3[contains(text(), 'Find your calling')]") 
    
    def __init__(self,driver):
        self.driver = driver
    def is_careers_page_loaded(self):
        return "careers" in self.get_current_url()
    def is_teams_block_displayed(self):
        return self.wait_element_visibility_of(15,self.TEAMS_BLOCK).is_displayed()
    def is_locations_block_displayed(self):
        return self.wait_element_visibility_of(15,self.LOCATIONS_BLOCK).is_displayed()
    def is_insiderat_life_block_displayed(self):
        return self.wait_element_visibility_of(15,self.LIFEATINSİDER_BLOCK).is_displayed()
    



    
        