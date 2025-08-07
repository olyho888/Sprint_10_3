import allure
from pages.create_recipe_page import CreateRecipePage
from pages.recipes_page import RecipesPage
from data import Data


class TestRecipesPage:

    @allure.title('Проверка создания рецепта')
    def test_recipes_page_create_recipe(self, auth):
        recipes_page = RecipesPage(auth)
        recipes_page.click_button_create_recipe()
        create_page = CreateRecipePage(auth)
        create_page.create_new_recipe(Data.RECIPE)
        recipe_element = recipes_page.get_recipe_card_element()
        recipe_title = recipes_page.get_recipe_title_text()
        assert recipe_element.is_displayed() and recipe_title == Data.RECIPE["Название рецепта"]
