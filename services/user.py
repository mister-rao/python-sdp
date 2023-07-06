"""
# snake_case - file names, variables, functions
# PascalCase - Class Names
-- import User model from models.py
-- create User Service Class
-- add a method signup to create new user
"""


"""
# for logging in user
user = User.get(username=username, password=password)

"""

from models import User


class UserService:
    def signup(self, username: str, password: str):
        user = User.create(username=username, password=password)
        print(f"{user.username} signed up!")

    def login(self, username: str, password: str):
        user = User.get(username=username, password=password)
        print(f"{user.username} logged in!")
