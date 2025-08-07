from selenium.webdriver.common.by import By
from locators.general_locators import GeneralLocators


class CreateAccountPageLocators(GeneralLocators):

    TITLE_REGISTRATION = (By.XPATH, "//*[contains(@class,'styles_title') and text()='Регистрация']")
    FIELD_FIRST_NAME = (By.XPATH, "//input[@name='first_name']")
    FIELD_LAST_NAME = (By.XPATH, "//input[@name='last_name']")
    FIELD_USERNAME = (By.XPATH, "//input[@name='username']")
    BUTTON_ACCOUNT = (By.XPATH, "//button[text()='Создать аккаунт']")
