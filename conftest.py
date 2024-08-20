from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# @pytest.fixture(scope="class") # class başında bir kere çalışır tüm testler koşar kapanır.
@pytest.fixture() # her test için çalışır
def setUp(request):
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    driver=webdriver.Chrome(options=chrome_options)
    driver.delete_all_cookies()
    driver.maximize_window()
    request.cls.driver = driver # bu fixture kullanan class lar driver çağırdığında driver = webdriver.Chrome() u ver dedik.  
    driver.implicitly_wait(15)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.failed:
        # Test başarısız olduğunda
        if "setUp" in item.funcargs:
            driver = item.funcargs["setUp"]
            screenshot_name = f"screenshot_{item.name}.png"
            driver.save_screenshot(screenshot_name)
            print(f"Ekran görüntüsü alındı: {screenshot_name}")
