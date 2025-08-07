import allure
from pages.authorization_page import AuthorizationPage
from pages.create_account_page import CreateAccountPage


class TestCreateAccountPage:

    @allure.title('Проверка регистрации пользователя')
    def test_create_account_page_check_registration(self, driver):
        auth_page = AuthorizationPage(driver)
        auth_page.open_authorization_page()
        auth_page.click_button_create_account()
        account_page = CreateAccountPage(driver)
        account_page.set_registration_data()
        current_url = auth_page.get_current_url()
        title_element = auth_page.get_registration_title_element()
        assert 'signin' in current_url and title_element.is_displayed()
