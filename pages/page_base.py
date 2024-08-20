from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Pagebase:
    def __init__(self,driver):
        self.driver = driver
    def wait_element_visibility_of(self,seconds,locator):
        element = WebDriverWait(self.driver,seconds).until(EC.visibility_of_element_located(locator))
        return element
    def wait_element_visibility_of_all(self,seconds,locator):
        element = WebDriverWait(self.driver,seconds).until(EC.visibility_of_all_elements_located(locator))
        return element
    def webelement_textini_ver(self,locator):
        return self.wait_element_visibility_of(20,locator).text
    def sayfa_url_ini_ver(self):
        return self.driver.current_url
    def wait_element_of_presence(self,seconds,locator):
        element = WebDriverWait(self.driver,seconds).until(EC.presence_of_element_located(locator))
        return element
    def wait_elements_of_presence(self,seconds,locator):
        element = WebDriverWait(self.driver,seconds).until(EC.presence_of_all_elements_located(locator))
        return element
    def wait_element_of_clickable(self, seconds, locator):
        element = WebDriverWait(self.driver,seconds).until(EC.element_to_be_clickable(locator))
        return element
    def get_current_url(self):
        return self.driver.current_url
    def get_title(self):
        return self.driver.title.lower()
    def close_cookies(self):
        try:
            cookies = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "wt-cli-accept-all-btn")))
            cookies.click()
        except:
            pass
    def get_nth_element(self, index, *locator):
        return self.driver.find_elements(*locator)[index]
    def hover_element(self, locator):
        element = self.wait_element_visibility_of(15, locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()