from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_web_page(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_present_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(ec.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def check_invisible_element(self, locator):
        invisible = WebDriverWait(self.driver, 15).until(ec.invisibility_of_element_located(locator))
        return invisible

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(locator))
        element = self.find_element_with_wait(locator)
        element.click()
        return element

    def send_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def send_text_to_present_element(self, locator, text):
        self.find_present_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def get_current_url(self):
        url = self.driver.current_url
        return url

    @staticmethod
    def format_locators(locators_1, value):
        method, locator = locators_1
        locator = locator.format(value)
        return method, locator
