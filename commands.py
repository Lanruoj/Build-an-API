from main import db
from flask import Blueprint
from main import bcrypt
from models.cards import Card
from models.users import User
from models.comments import Comment
from datetime import date


db_commands = Blueprint('db', __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")


@db_commands.cli.command("seed")
def seed_db():
    # MUST CREATE USERS FIRST AS user_id IS FK FOR cards
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
    # MUST ALSO COMMIT CHANGES SO THAT THE users EXIST PRIOR TO SEEDING cards
    db.session.commit()

    card1 = Card(
                title = "Wake up",
                description = "Get out of bed",
                date = date.today(),
                status = "WIP",
                priority = "High",
                user_id = test_user.id
    )
    db.session.add(card1)

    card2 = Card(
                title = "Feed Archie",
                description = "Give Archie one scoop of dry food",
                date = date.today(),
                status = "Done",
                priority = "High",
                user_id = test_user.id
    )
    db.session.add(card2)

    db.session.commit()

    comment1 = Comment(
                        message = "First test comment on card 1",
                        user = test_user,
                        card = card1
    )
    db.session.add(comment1)

    comment2 = Comment(
                        message = "First test comment on card 2",
                        user = test_user,
                        card = card2
    )
    db.session.add(comment2)

    comment3 = Comment(
                        message = "Second test comment on card 1",
                        user = test_user,
                        card = card1
    )
    db.session.add(comment3)

    db.session.commit()

    print("Tables seeded")


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")