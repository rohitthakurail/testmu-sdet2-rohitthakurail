import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):

    browser = getattr(request, "param", "chrome")

    if browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    yield driver

    driver.quit()