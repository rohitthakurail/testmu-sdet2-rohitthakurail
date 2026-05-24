import json
import pytest
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.settings import BASE_UI_URL
from utils.logger import setup_logger

logger = setup_logger()


@allure.feature('Login')
@pytest.mark.smoke
@pytest.mark.cross_browser
@pytest.mark.parametrize("driver", ["chrome", "firefox"],
                         indirect=True)
def test_login(driver):
    """
    Test login flow, form validation and cross browser execution
    """
    logger.info("Testing Login Flow...")
    driver.get(BASE_UI_URL)

    with open('data/ui/ui_data.json') as f:
        data = json.load(f)

    logger.info("Login with credentials..")
    login_page = LoginPage(driver)
    login_page.verify_on_login_page()
    login_page.login(data['ui_username'], data['ui_password'])

    dashboard = DashboardPage(driver)
    actual_title = dashboard.get_dashboard_title()
    assert actual_title == dashboard.TITLE_TEXT, \
        f"Expected Dashboard Title {dashboard.TITLE_TEXT} is different from actual Title found {actual_title}"
    logger.info("Logged in successfully")
