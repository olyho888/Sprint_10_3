import allure
from locators.authorization_page_locators import AuthorizationPageLocators
from pages.base_page import BasePage
from data import Data


class AuthorizationPage(BasePage):

    @allure.step('Открываем страницу авторизации')
    def open_authorization_page(self):
        self.open_web_page(Data.AUTH_URL)
        self.find_element_with_wait(AuthorizationPageLocators.TITLE_LOGIN_TO_SITE)

    @allure.step('Кликаем на кнопку Создать аккаунт')
    def click_button_create_account(self):
        self.click_to_element(AuthorizationPageLocators.BUTTON_CREATE_ACCOUNT)
        self.check_invisible_element(AuthorizationPageLocators.TITLE_LOGIN_TO_SITE)

    @allure.step('Заполняем данными форму Авторизации')
    def set_registration_data(self, data):
        self.find_element_with_wait(AuthorizationPageLocators.TITLE_LOGIN_TO_SITE)
        self.send_text_to_element(AuthorizationPageLocators.FIELD_EMAIL, data["email"])
        self.send_text_to_element(AuthorizationPageLocators.FIELD_PASSWORD, data["password"])
        self.click_to_element(AuthorizationPageLocators.BUTTON_ENTER)
        self.check_invisible_element(AuthorizationPageLocators.TITLE_LOGIN_TO_SITE)

    @allure.step('Получаем элемент заголовка Войти на сайт')
    def get_registration_title_element(self):
        element = self.find_element_with_wait(AuthorizationPageLocators.TITLE_LOGIN_TO_SITE)
        return element
