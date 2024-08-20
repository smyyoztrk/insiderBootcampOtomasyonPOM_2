from selenium.webdriver.common.by import By
from time import sleep
from pages.page_base import Pagebase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class QAPage(Pagebase):
    QA_URL = "https://useinsider.com/careers/quality-assurance/"
    SEE_ALL_QA_JOBS_BUTTON = (By.CSS_SELECTOR,"div[class='button-group d-flex flex-row']>a")
    LOCATION_FILTER = (By.CSS_SELECTOR, "span[id='select2-filter-by-location-container']")
    DEPARTMENT_FILTER = (By.CSS_SELECTOR, "span[id='select2-filter-by-department-container']")
    QUALİTY_ASSURANCE = (By.XPATH, "//li[contains (text(), 'Quality Assurance')]")
    JOBS_LIST = (By.CSS_SELECTOR, "div[class='position-list-item col-12 col-lg-4 qualityassurance istanbul-turkey full-timeremote']")

    def __init__(self,driver):
        self.driver = driver
    def load(self):
        self.driver.get(self.QA_URL)
    def filter_jobs(self, location, department):
        self.close_cookies()
        actions = ActionChains(self.driver)
        see_qa_jobs_button_element = self.wait_element_of_clickable(15,self.SEE_ALL_QA_JOBS_BUTTON)
        self.driver.execute_script("arguments[0].click();", see_qa_jobs_button_element)
        self.driver.execute_script("window.scrollBy(0,300)","")
        sleep(10)
        location_filter_element = self.wait_element_visibility_of(30,self.LOCATION_FILTER).click()
        LOCATION = (By.XPATH, f"//li[text()='{location}']")
        DEPARTMENT = (By.XPATH, f"//li[text()='{department}']")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//li[text()='{location}']"))).click()
        self.wait_element_visibility_of(15,self.DEPARTMENT_FILTER).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//li[text()='{department}']"))).click()
    def are_jobs_listed(self):
        return len(self.wait_element_visibility_of_all(15,self.JOBS_LIST)) > 0
    def is_job_list_correct(self, position_text, department_text, location_text):
        jobs = self.wait_element_visibility_of_all(20,self.JOBS_LIST)
        for job in jobs:
            if position_text not in job.text or department_text not in job.text or location_text not in job.text:
                return False
        return True

        
       

        
    



