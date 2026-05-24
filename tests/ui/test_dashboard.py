import json
import pytest
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.settings import BASE_UI_URL
from utils.logger import setup_logger

logger = setup_logger()


@allure.feature('Dashboard')
@pytest.mark.smoke
def test_sorting_inventory(driver):
    """
    Test Sorting of items on basis of prices Low to High
    :param driver:
    """
    logger.info("Testing Sorting of items on dashboard...")
    driver.get(BASE_UI_URL)
    # load credentials
    with open('data/ui/ui_data.json') as f:
        data = json.load(f)
    logger.info("Login with credentials...")
    # login
    login_page = LoginPage(driver)
    login_page.verify_on_login_page()
    login_page.login(data['ui_username'], data['ui_password'])

    dashboard = DashboardPage(driver)
    logger.info("Sorting Inventory items based on price low to high...")
    # sorting items -> Price Low to High
    dashboard.sort_items_by_price_l2h()
    # verify sorting
    price_list = dashboard.get_price_of_inventory_items()
    assert price_list == sorted(price_list)
    logger.info("Inventory items sorted Successfully!")
