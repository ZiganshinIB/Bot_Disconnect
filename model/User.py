import sqlite


async def get_user(user_id: str):
    pass


async def set_user(user_id, state):
    pass


class User():
    user_id: str
    name: str
    gender: bool
    description: str

    def __init__(self, id):
        self.user_id = id

    def set_name(self, name: str) -> None:
        self.name = name

    def set_gender(self, gender: bool) -> None:
        self.gender = gender

    def set_description(self, description: str) -> None:
        self.description = description

    def set_all(self, name: str, gender: bool, description: str) -> None:
        self.name = name
        self.gender = gender
        self.description = description
