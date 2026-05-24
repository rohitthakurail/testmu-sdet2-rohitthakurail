from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        """
        Method to find an element. If found multiple elements then it will return first one.
        :param locator: By
        :return: WebElement
        """
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))

    def get_elements(self, locator):
        """
        Method to find multiple elements with single locator
        :param locator: By
        :return: List[WebElement]
        """
        return self.driver.find_elements(*locator)

    def click(self, locator):
        """
        Method to click the first element found with locator
        :param locator: By
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type(self, locator, text):
        """
        Method to fill text in element like input, form etc.
        :param locator: By
        :param text: String
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        Method to extract the text from a web element
        :param locator: By
        :return: String
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text
