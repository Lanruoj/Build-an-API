from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    # USING A LIST COMPREHENSION AND MULTIPLE ASSIGNMENT TO GET THE ENVIRONMENT VARIABLES WE NEED

    # CREATING THE FLASK app OBJECT - OUR APP!
    app = Flask(__name__)

    # CONFIGURING OUR APP
    app.config.from_object("config.app_config")

    # CREATING OUR DATABASE OBJECT - THIS ALLOWS US TO USE OUR ORM
    db = SQLAlchemy(app)

    # THIS IS OUR CONSTRUCTED APP!
    return app

@app.route('/')
def hello_world():
    return "Hello, world!"