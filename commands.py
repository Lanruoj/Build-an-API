from main import db
from flask import Blueprint
from main import bcrypt
from models.cards import Card
from models.users import User
from datetime import date


db_commands = Blueprint('db', __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Table created")


@db_commands.cli.command("seed")
def seed_db():
    card1 = Card(
                title = "Wake up",
                description = "Get out of bed",
                date = date.today(),
                status = "WIP",
                priority = "High"
    )
    db.session.add(card1)

    card2 = Card(
                title = "Feed Archie",
                description = "Give Archie one scoop of dry food",
                date = date.today(),
                status = "Done",
                priority = "High"
    )
    db.session.add(card2)

    admin = User(
                name = "admin",
                email = "admin@email.com",
                password = bcrypt.generate_password_hash("admin123").decode("utf-8"),
                admin = True
    )
    db.session.add(admin)

    test_user = User(
                    name = "test user",
                    email = "test@email.com",
                    password = bcrypt.generate_password_hash("test123").decode("utf-8")
    )
    db.session.add(test_user)

    db.session.commit()

    print("Tables seeded")


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")