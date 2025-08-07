from selenium.webdriver.common.by import By
from locators.general_locators import GeneralLocators


class AuthorizationPageLocators(GeneralLocators):

    TITLE_LOGIN_TO_SITE = (By.XPATH, "//*[contains(@class,'styles_title') and text()='Войти на сайт']")
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")
