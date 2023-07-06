import typer
from services.user import UserService

app = typer.Typer()

user_service = UserService()
"""
# for logging in user
user = User.get(username=username, password=password)
"""


@app.command()
def signup(username: str, password: str):
    user_service.signup(username, password)


@app.command()
def login(username: str, password: str):
    user_service.login(username, password)
