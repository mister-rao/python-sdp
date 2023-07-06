import typer
from models import create_tables
from commands import inventory
from commands import user

app = typer.Typer()

app.add_typer(inventory.app, name="inventory")
app.add_typer(user.app, name="user")

if __name__ == "__main__":
    create_tables()
    app()
