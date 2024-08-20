from selenium.webdriver.common.by import By
from time import sleep
from pages.page_base import Pagebase
from selenium.webdriver.common.action_chains import ActionChains

class ViewRolePage(Pagebase):
    VİEW_ROLE_BUTTON_LIST = (By.CSS_SELECTOR, "a[class='btn btn-navy rounded pt-2 pr-5 pb-2 pl-5']")
    APPLICATION_FORM = (By.CSS_SELECTOR, "a[class='postings-btn template-btn-submit shamrock']:nth-child(1)")

    def __init__(self,driver):
        self.driver = driver
    def click_view_role(self):
        actions = ActionChains(self.driver)
        view_role_button = self.get_nth_element(0, *self.VİEW_ROLE_BUTTON_LIST)
        actions.move_to_element(view_role_button).click().perform()
        sleep(10)
    def is_redirected_to_application_form(self):
        # Mevcut pencere kimliğini sakla
        main_window_handle = self.driver.current_window_handle
        
        # Yeni pencere/sekme kimliğine geçiş yap
        all_window_handles = self.driver.window_handles
        for handle in all_window_handles:
            if handle != main_window_handle:
                self.driver.switch_to.window(handle)
                break
        element = self.wait_element_visibility_of(30,self.APPLICATION_FORM)
        return element.is_displayed()
        # return 'lever' in self.get_current_url()
