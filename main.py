from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():
    # USING A LIST COMPREHENSION AND MULTIPLE ASSIGNMENT TO GET THE ENVIRONMENT VARIABLES WE NEED

    # CREATING THE FLASK app OBJECT - OUR APP!
    app = Flask(__name__)
    
    # CONFIGURING OUR APP
    app.config.from_object("config.app_config")

    # CREATING OUR DATABASE OBJECT - THIS ALLOWS US TO USE OUR ORM
    db.init_app(app)

    # CREATING OUR MARSHMALLOW OBJECT
    ma.init_app(app)

    # CREATING OUR BCRYPT OBJECT
    bcrypt.init_app(app)

    # CREATING OUR JWT OBJECT
    jwt.init_app(app)

    # IMPORT CLI COMMANDS FROM commands.py
    from commands import db_commands
    app.register_blueprint(db_commands)

    # IMPORT THE CONTROLLERS FROM controllers.py AND ACTIVATE THE BLUEPRINTS
    from controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)

    # THIS IS OUR CONSTRUCTED APP!
    return app