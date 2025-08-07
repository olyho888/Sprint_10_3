import pytest
from selenium import webdriver
from pages.authorization_page import AuthorizationPage
from data import Data


@pytest.fixture(params=["remote"])
def driver(request):
    if request.param == "local":
        driver = webdriver.Chrome()
    else:
        options = webdriver.ChromeOptions()
        driver = webdriver.Remote("http://selenoid:4444/wd/hub", options=options)
    driver.set_window_size(1920,1080)
    yield driver
    driver.quit()

@pytest.fixture
def auth(driver):
    auth_page = AuthorizationPage(driver)
    auth_page.open_authorization_page()
    auth_page.set_registration_data(Data.USER)
    return driver
