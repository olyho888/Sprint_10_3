# Sprint_10_3

Автотесты для сервиса «Продуктовый помощник»(https://foodgram-frontend-1.prakticum-team.ru/signin)

Основа для написания автотестов — фреймворк pytest, Selenium
Автотесты запускаются в браузере Chrome

Проект состоит из:

директории assets - содержит файл загружаемый на сервер

директории Locators - содержит описание локаторов на страницах
authorization_page_locators - описаны локаторы страницы authorization_page
create_account_page_locators - описаны локаторы страницы create_account_page
create_recipe_page_locators - описаны локаторы страницы create_recipe_page
general_locators - описаны общие локаторы 
recipes_page_locators - описаны локаторы страницы recipes_page

директории Pages - содержит описание методов на страницах
base_page - описание базовых методов 
authorization_page - описание выполняемых методов на странице authorization_page
create_account_page - описаны выполняемых методов на странице create_account_page
create_recipe_page - описание выполняемых методов на странице create_recipe_page
recipes_page - описание выполняемых методов на странице recipes_page

директория Tests - содержит описание тестов на страницах

test_authorization_page - содержит тест:
- test_authorization_page_check_login - тест на проверку авторизации пользователя

test_create_account_page - содержит тест:
- test_create_account_page_check_registration - тест на проверку регистрации пользователя

test_recipes_page - содержит тест:
- test_recipes_page_create_recipe - тест на проверку создания рецепта

директория allure-report - содержит отчет о результатах выполнения тестов, сгенерированный с посмощью фреймворк Allure

Dockerfile - содержит инструкции для сборки докер образа проекта с тестами
docker-compose.yam - содержит конфигурацию докер контейнеров для сборки проекта с Selenoid
config.json - содержит конфигурацию для докер контейнера с браузером Chrome
ci.yml - содержит команды для сборки проекта с CI/CD на базе GitHub Actions
