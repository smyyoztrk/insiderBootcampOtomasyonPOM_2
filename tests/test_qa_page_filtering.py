import pytest
import softest
from time import sleep
from pages.qa_page import QAPage

@pytest.mark.usefixtures("setUp")
class TestQaPageFiltering(softest.TestCase):
    def test_qa_jobs_are_listed(self):
        qapage = QAPage(self.driver)
        qapage.load()
        qapage.filter_jobs(location="Istanbul, Turkey", department="Quality Assurance")
        self.soft_assert(self.assertTrue, qapage.are_jobs_listed(), "No QA jobs are listed")
    
        
        
        

