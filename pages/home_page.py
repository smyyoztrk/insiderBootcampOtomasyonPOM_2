from selenium.webdriver.common.by import By
from pages.page_base import Pagebase

class HomePage(Pagebase):
    BASE_URL = "https://useinsider.com/"
    COMPANY_MENU = (By.XPATH,"//a[contains (text() , 'Company')]")
    CAREERS = (By.XPATH,"//a[contains (text(),'Careers')]")

    def __init__(self,driver):
        self.driver = driver
        
    def load(self):
        self.driver.get(self.BASE_URL)
        self.close_cookies()
    def is_loaded(self):
        return "insider".lower() in self.get_current_url() and self.get_title()
    def click_menu_item(self,menuName):
        self.wait_element_visibility_of(15,menuName).click()
    def go_to_careers(self):
        self.wait_element_visibility_of(15,self.CAREERS).click()


    
