from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_LOC = (By.ID, 'user-name')
    PASSWORD_LOC = (By.ID, 'password')
    LOGIN_BTN_LOC = (By.ID, 'login-button')

    def login(self, username, password):
        """
        Method to login on https://www.saucedemo.com
        :param username:
        :param password:
        """
        self.type(self.USERNAME_LOC, username)
        self.type(self.PASSWORD_LOC, password)
        self.click(self.LOGIN_BTN_LOC)