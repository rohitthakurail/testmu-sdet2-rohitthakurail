import json
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.settings import BASE_UI_URL
from utils.api_client import APIClient
from utils.logger import setup_logger

logger = setup_logger()


@allure.feature('Integration')
def test_sorting_inventory_wrt_booking_id(driver):
    """
    Test Sorting of items on basis of booking ID returned by API response
    If ID is odd -> sort by prices Low to High
    ID is even -> sort by prices High to Low
    :param driver:
    """
    logger.info("Running Integration test")
    driver.get(BASE_UI_URL)
    # load credentials
    with open('data/ui/ui_data.json') as f:
        data = json.load(f)
    logger.info("Login with credentials")
    # login
    login_page = LoginPage(driver)
    login_page.verify_on_login_page()
    login_page.login(data['ui_username'], data['ui_password'])

    dashboard = DashboardPage(driver)
    logger.info("Creating Booking ID....")
    booking_id = APIClient().create_booking_id()
    logger.info(f"Booking ID created: {booking_id}")
    if booking_id % 2 == 0:
        logger.info("Booking ID is even, sorting inventory by price high to low")
        # sorting items -> price high to low
        dashboard.sort_items_by_price_h2l()
        # verify sorting
        price_list = dashboard.get_price_of_inventory_items()
        assert price_list == sorted(price_list, reverse=True), "Sorting Failed!"
        logger.info("Sorted successfully")
    else:
        logger.info("Booking ID is odd, sorting inventory by price low to high")
        # sorting items -> Price Low to High
        dashboard.sort_items_by_price_l2h()
        # verify sorting
        price_list = dashboard.get_price_of_inventory_items()
        assert price_list == sorted(price_list), "Sorting Failed"
        logger.info("Sorted successfully")
