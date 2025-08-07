import allure
from locators.recipes_page_locators import RecipesPageLocators
from pages.base_page import BasePage


class RecipesPage(BasePage):

    @allure.step('Получаем элемент кнопки Выход')
    def get_exit_button_element(self):
        element = self.find_element_with_wait(RecipesPageLocators.BUTTON_EXIT)
        return element

    @allure.step('Кликаем на кнопку Создать рецепт')
    def click_button_create_recipe(self):
        self.click_to_element(RecipesPageLocators.BUTTON_CREATE_RECIPE)
        self.check_invisible_element(RecipesPageLocators.TITLE_RECIPES)

    @allure.step('Получаем элемент карточки рецепта')
    def get_recipe_card_element(self):
        element = self.find_element_with_wait(RecipesPageLocators.RECIPE_CARD)
        return element

    @allure.step('Получаем заголовок рецепта')
    def get_recipe_title_text(self):
        text = self.get_text_from_element(RecipesPageLocators.TITLE_RECIPE_CARD)
        return text
