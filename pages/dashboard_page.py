import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class DashboardPage(BasePage):
    TITLE_TEXT = 'Swag Labs'
    TITLE_LOC = (By.CLASS_NAME, 'app_logo')
    SORTING_LOC = (By.CLASS_NAME, 'product_sort_container')
    INVENTORY_ITEMS_LOC = (By.CLASS_NAME, 'inventory_item')
    ITEM_PRICE_LOC = (By.CLASS_NAME, 'inventory_item_price')
    LOGOUT_BTN_LOC = (By.ID, 'logout_sidebar_link')

    def get_dashboard_title(self) -> str:
        """
        Method to return the Title of dashboard page.
        """
        return self.get_text(self.TITLE_LOC)

    def sort_items_by_price_l2h(self):
        """
        Method to sorting of items on basis of Price (Low to High)
        """
        # Get the Element used for sorting
        sorting_element = self.get_element(self.SORTING_LOC)
        # Selecting value By Price Low to High
        Select(sorting_element).select_by_value('lohi')
        time.sleep(1)

    def sort_items_by_price_h2l(self):
        """
        Method to sorting of items on basis of Price (Low to High)
        """
        # Get the Element used for sorting
        sorting_element = self.get_element(self.SORTING_LOC)
        # Selecting value By Price Low to High
        Select(sorting_element).select_by_value('hilo')
        time.sleep(1)

    def get_price_of_inventory_items(self) -> list:
        """
        Method to return the list of prices of all items on a page
        :return: List
        """
        item_list = self.get_elements(self.ITEM_PRICE_LOC)
        return [float(i.text.replace('$','')) for i in item_list]

    def logout(self):
        """
        Method to logout
        """
        self.click(self.LOGOUT_BTN_LOC)

