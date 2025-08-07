import allure
from pages.authorization_page import AuthorizationPage
from pages.create_account_page import CreateAccountPage
from pages.recipes_page import RecipesPage
from data import Data


class TestAuthorizationPage:

    @allure.title('Проверка авторизации пользователя')
    def test_authorization_page_check_login(self, driver):
        account_page = CreateAccountPage(driver)
        account_page.open_registration_page()
        account_page.click_button_login()
        auth_page = AuthorizationPage(driver)
        auth_page.set_registration_data(Data.USER)
        recipes_page = RecipesPage(driver)
        current_url = recipes_page.get_current_url()
        exit_element = recipes_page.get_exit_button_element()
        assert 'recipes' in current_url and exit_element.is_displayed()
