from flask import Flask

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///blog.db'
app.secret_key = 'secret key'

CORS(app)

from sweater import models,routes

db.create_all()