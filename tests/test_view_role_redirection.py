import pytest
import softest
from time import sleep
from pages.view_role_page import ViewRolePage
from pages.qa_page import QAPage

@pytest.mark.usefixtures("setUp")
class TestViewRoleRedirection(softest.TestCase):
    def test_view_role_redirects_to_application_form(self):
        qapage = QAPage(self.driver)
        qapage.load()
        qapage.filter_jobs(location="Istanbul, Turkey", department="Quality Assurance")
        viewrolepage = ViewRolePage(self.driver)
        viewrolepage.click_view_role()
        assert viewrolepage.is_redirected_to_application_form(), "View Role does not redirect to the application form!"