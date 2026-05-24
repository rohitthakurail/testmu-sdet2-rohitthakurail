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

    def verify_dashboard_title(self):
        """
        Method to verify the Title of dashboard page.
        """
        actual_title = self.get_text(self.TITLE_LOC)
        assert self.get_text(self.TITLE_LOC) == self.TITLE_TEXT, \
            f"Expected Dashboard Title {self.TITLE_TEXT} is different from actual Title found {actual_title}"

    def sort_items_by_price_l2h(self):
        """
        Method to sorting of items on basis of Price (Low to High)
        """
        # Get the Element used for sorting
        sorting_element = self.get_element(self.SORTING_LOC)
        # Selecting value By Price Low to High
        Select(sorting_element).select_by_value('lohi')

    def get_price_of_inventory_items(self):
        """
        Method to return the list of prices of all items on a page
        :return: List
        """
        item_list = self.get_elements(self.ITEM_PRICE_LOC)
        return [i.text.replace('$','')for i in item_list]

    def logout(self):
        """
        Method to logout
        """
        self.click(self.LOGOUT_BTN_LOC)

