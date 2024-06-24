from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime


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

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    questions = db.relationship('Question', backref='quiz', lazy=True)

    def __repr__(self):
        return f'<Quiz {self.title}, Category: {self.category}>'

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    answers = db.relationship('Answer', backref='question', lazy=True)

    def __repr__(self):
        return f'<Question {self.text[:50]}...>'

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)

    def __repr__(self):
        return f'<Answer {self.text[:50]}..., Correct: {self.is_correct}>'

class QuizResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    date_taken = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<QuizResult User: {self.user_id}, Quiz: {self.quiz_id}, Score: {self.score}>'
