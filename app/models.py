from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12), index=True, unique=True, nullable=False)
    email = db.Column(db.String(25), index=True, unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    img = db.Column(db.String(20), nullable=False, default='default.jpg')
  
    def __repr__(self):
        return f'<User {self.username}, {self.email}, {self.img}>'
