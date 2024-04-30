from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
#created database variable 
DB_NAME = "database.db"
#defining the name of the database

def create_app():
    #Creates the flask app
    app = Flask(__name__)
    #Name is the module we are running to create the app
    app.config['SECRET_KEY'] = "helloworld"
    #This encrypts the session data
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    #configure database 
    #"f' shows the path to the database

    from .views import views
    #pulling file view.py so we can register the blueprint. 
    from .auth import auth
    #pulling file auth.py so we can register the blueprint. 
    from .models import User, Post
    #pulling file models so we can register the blueprint. 
    from . import models 

    with app.app_context():
        db.create_all() 

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

 


    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


