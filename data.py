class Data:


    BASE_URL = 'https://foodgram-frontend-1.prakticum-team.ru'
    AUTH_URL = 'https://foodgram-frontend-1.prakticum-team.ru/signin'
    ACCOUNT_URL = 'https://foodgram-frontend-1.prakticum-team.ru/signup'

    USER = {
        "email": "test10500@yandex.ru",
        "password": "olyho123456",
    }

    RECIPE = {
        "Название рецепта": "Бутерброд",
        "Теги": ("Завтрак", "Обед"),
        "Ингредиенты": [
            ("варенье", 10),
            ("сливочное масло", 5),
            ("хлеб белый сухой", 20)
        ],
        "Время приготовления": 3,
        "Описание рецепта": "Лучше взять клубничное варенье, так будет вкуснее",
        "Фото": "buter.jpg"
    }
