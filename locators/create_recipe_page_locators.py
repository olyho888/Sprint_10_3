from selenium.webdriver.common.by import By
from locators.general_locators import GeneralLocators


class CreateRecipePageLocators(GeneralLocators):

    TITLE_CREATE_RECIPE = (By.XPATH, "//*[contains(@class,'styles_title') and text()='Создание рецепта']")
    NAME_RECIPE = (By.XPATH, "//*[text()='Название рецепта']/../input")
    TAG_CHECKBOX = (By.XPATH, "//*[text()='{}']/..//*[contains(@class,'styles_checkbox')]")
    INGREDIENTS = (By.XPATH, "//*[text()='Ингредиенты']/../input")
    INGREDIENT_CHOICE = (By.XPATH, "//*[contains(@class,'styles_container')]/*[text()='{}']")
    WEIGHT = (By.XPATH, "//*[contains(@class,'styles_ingredientsAmount')]/../input")
    ADD_INGREDIENT = (By.XPATH, "//*[contains(@class,'styles_ingredientAdd') and text()='Добавить ингредиент']")
    COOKING_TIME = (By.XPATH, "//*[text()='Время приготовления']/../input")
    RECIPE_DESCRIPTION = (By.XPATH, "//*[text()='Описание рецепта']/../textarea")
    INPUT_FILE = (By.XPATH, "//*[contains(@class,'styles_fileInput') and @type='file']")
    BUTTON_CREATE_RECIPE = (By.XPATH, "//*[contains(@class,'style_button') and text()='Создать рецепт']")
