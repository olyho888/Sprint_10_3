from selenium.webdriver.common.by import By
from locators.general_locators import GeneralLocators


class RecipesPageLocators(GeneralLocators):

    BUTTON_CREATE_RECIPE = (By.XPATH, "//*[contains(@class,'style_link') and text()='Создать рецепт']")
    BUTTON_EXIT = (By.XPATH, "//*[contains(@class,'styles_menuLink') and text()='Выход']")
    TITLE_RECIPES = (By.XPATH, "//*[contains(@class,'styles_title') and text()='Рецепты']")
    TITLE_RECIPE_CARD = (By.XPATH, "//*[contains(@class,'styles_single-card__title')]")
    RECIPE_CARD = (By.XPATH, "//*[contains(@class,'style_container')]/*[contains(@class,'styles_single-card')]")
