from datetime import datetime

class User:

    def __init__(self, user_id: int, name: str, surname: str, age: int, email: str, register_date: str):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.register_date = register_date