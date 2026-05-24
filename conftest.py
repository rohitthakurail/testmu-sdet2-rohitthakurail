from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver(request):

    browser = getattr(request, "param", "chrome")

    if browser == "firefox":
        driver = webdriver.Firefox()
    else:
        options = Options()
        options.add_argument("--guest")
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