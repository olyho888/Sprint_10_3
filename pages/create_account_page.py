import allure
from locators.create_account_page_locators import CreateAccountPageLocators
from pages.base_page import BasePage
from data import Data
from helpers import Helpers


class CreateAccountPage(BasePage):

    @allure.step('Открываем страницу регистрации')
    def open_registration_page(self):
        self.open_web_page(Data.ACCOUNT_URL)
        self.find_element_with_wait(CreateAccountPageLocators.TITLE_REGISTRATION)

    @allure.step('Кликаем на кнопку Войти')
    def click_button_login(self):
        self.click_to_element(CreateAccountPageLocators.BUTTON_LOGIN)
        self.check_invisible_element(CreateAccountPageLocators.TITLE_REGISTRATION)

    @allure.step('Заполняем данными форму Регистрация')
    def set_registration_data(self, data=None):
        if data is None:
            user = Helpers.generate_user_data()
        else:
            user = dict(data)
        self.find_element_with_wait(CreateAccountPageLocators.TITLE_REGISTRATION)
        self.send_text_to_element(CreateAccountPageLocators.FIELD_FIRST_NAME, user["first_name"])
        self.send_text_to_element(CreateAccountPageLocators.FIELD_LAST_NAME, user["last_name"])
        self.send_text_to_element(CreateAccountPageLocators.FIELD_USERNAME, user["username"])
        self.send_text_to_element(CreateAccountPageLocators.FIELD_EMAIL, user["email"])
        self.send_text_to_element(CreateAccountPageLocators.FIELD_PASSWORD, user["password"])
        self.click_to_element(CreateAccountPageLocators.BUTTON_ACCOUNT)
        self.check_invisible_element(CreateAccountPageLocators.TITLE_REGISTRATION)
        return user
