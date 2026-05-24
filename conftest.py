from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture
def driver(request):

    browser = getattr(request, "param", "chrome")

    if browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox()
    else:
        options = Options()
        options.add_argument("--guest")
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            driver.save_screenshot(
                f"reports/screenshots/{timestamp}.png"
            )