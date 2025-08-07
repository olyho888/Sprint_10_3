import allure
from locators.create_recipe_page_locators import CreateRecipePageLocators
from pages.base_page import BasePage
from helpers import Helpers


class CreateRecipePage(BasePage):

    @allure.step('Создаём рецепт')
    def create_new_recipe(self, data):
        self.find_element_with_wait(CreateRecipePageLocators.TITLE_CREATE_RECIPE)
        self.send_text_to_element(CreateRecipePageLocators.NAME_RECIPE, data["Название рецепта"])
        for key in ("Завтрак", "Обед", "Ужин"):
            if key not in data["Теги"]:
                locator=self.format_locators(CreateRecipePageLocators.TAG_CHECKBOX, key)
                self.click_to_element(locator)
        for value in data["Ингредиенты"]:
            self.send_text_to_element(CreateRecipePageLocators.INGREDIENTS, value[0])
            locator = self.format_locators(CreateRecipePageLocators.INGREDIENT_CHOICE, value[0])
            self.click_to_element(locator)
            self.send_text_to_element(CreateRecipePageLocators.WEIGHT, value[1])
            self.click_to_element(CreateRecipePageLocators.ADD_INGREDIENT)
        self.send_text_to_element(CreateRecipePageLocators.COOKING_TIME, data["Время приготовления"])
        self.send_text_to_element(CreateRecipePageLocators.RECIPE_DESCRIPTION, data["Описание рецепта"])
        file = f'{Helpers.get_app_dir()}/assets/{data["Фото"]}'
        self.send_text_to_present_element(CreateRecipePageLocators.INPUT_FILE, file)
        self.click_to_element(CreateRecipePageLocators.BUTTON_CREATE_RECIPE)
        self.check_invisible_element(CreateRecipePageLocators.TITLE_CREATE_RECIPE)
