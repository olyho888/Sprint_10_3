import pathlib
import random
import string


class Helpers:

    @staticmethod
    def generate_random_string(length):
        characters = string.ascii_lowercase
        random_string = ''
        for i in range(length):
            random_string += random.choice(characters)
        return random_string

    @staticmethod
    def generate_user_data():
        username = Helpers.generate_random_string(7)
        user_data = {
            'first_name': Helpers.generate_random_string(7),
            'last_name': Helpers.generate_random_string(7),
            'username': username,
            'email': f"{username}@yandex.ru",
            'password': Helpers.generate_random_string(8)
        }
        return user_data

    @staticmethod
    def get_app_dir():
        app_dir = pathlib.Path(__file__).parent
        result = str(app_dir).replace('\\','/')
        return result
