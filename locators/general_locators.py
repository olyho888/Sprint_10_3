from selenium.webdriver.common.by import By


class GeneralLocators:

    BUTTON_CREATE_ACCOUNT = (By.XPATH, "//*[contains(@class,'styles_menuButton') and text()='Создать аккаунт']")
    BUTTON_LOGIN = (By.XPATH, "//*[contains(@class, 'styles_menuLink') and text()='Войти']")
    FIELD_EMAIL = (By.XPATH, "//input[@name='email']")
    FIELD_PASSWORD = (By.XPATH, "//input[@name='password']")
