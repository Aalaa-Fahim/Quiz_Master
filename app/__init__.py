from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '70678d4c4f51674c3974bfccdff5b7b2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./new_add_q.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./quiz.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./question_test.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./app_data_new.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./app_data.db'
csrf = CSRFProtect(app)
db= SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'primary'

from app import routes, models
