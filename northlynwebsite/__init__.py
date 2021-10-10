# northlynwebsite/__init__.py
import os, re
uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
   uri = uri.replace("postgres://", "postgresql://", 1)
# rest of connection code using the connection string `uri`

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

### Database setup #####
#basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/northlyn'
app.config['SQLALCHEMY_DATABASE_URI'] = uri

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

#### Login CONFIGURATIONS #####

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

######### blueprints ##########

from northlynwebsite.core.views import core
from northlynwebsite.users.views import users
from northlynwebsite.error_pages.handlers import error_pages
from northlynwebsite.char.views import char
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
app.register_blueprint(char)
