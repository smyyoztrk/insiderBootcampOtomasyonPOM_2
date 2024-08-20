import pytest
import softest
from time import sleep
from pages.qa_page import QAPage

@pytest.mark.usefixtures("setUp")
class TestPositionVerify(softest.TestCase):
    def test_position_information_is_correct(self):
        qapage = QAPage(self.driver)
        qapage.load()
        qapage.filter_jobs(location="Istanbul, Turkey", department="Quality Assurance")
        assert qapage.is_job_list_correct("Quality Assurance", "Quality Assurance", "Istanbul, Turkey"), "Job listings information is incorrect!"




