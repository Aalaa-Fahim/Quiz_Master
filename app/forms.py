from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField, RadioField, BooleanField, SelectField, TextAreaField, HiddenField, IntegerField, FieldList, FormField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User, Quiz, Question, Answer, QuizResult, InputQuestion, InputAnswer
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4, max=12)])
    email = StringField('Email Address',
                        validators=[DataRequired(), Email(), Length(min=14, max=30)])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=4, max=16)])
    password_confirm = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit_btn = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username already exists!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email already exists!')


class LoginForm(FlaskForm):
    email = StringField('Email Address',
                        validators=[DataRequired(), Email(), Length(min=14, max=30)])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=4, max=16)])
    remember = BooleanField('Remember me')
    submit_btn = SubmitField('Login')


class UpdateForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4, max=12)])
    email = StringField('Email Address',
                        validators=[DataRequired(), Email(), Length(min=14, max=30)])
    profile_pic = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit_btn = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username already exists! Try Again.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email already exists! Try Again.')

class QuizSelectCatForm(FlaskForm):
    category = SelectField('Category', choices=[('history', 'History'), ('science', 'Science'), ('programming', 'Programming')], validators=[DataRequired()])
    submit_btn = SubmitField('Start Quiz')


class QuizForm(FlaskForm):
    answer = SelectField('Answer', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit')

class InputQuestionForm(FlaskForm):
    question = TextAreaField('Question', validators=[DataRequired()])
    category = SelectField('Category', choices=[('History', 'History'), ('Science', 'Science'), ('Programming', 'Programming')], validators=[DataRequired()])
    #quiz_id = HiddenField('Quiz ID', validators=[DataRequired()])
    submit = SubmitField('Add a Question')


class InputAnswerForm(FlaskForm):
    question_id = IntegerField('Question ID', validators=[DataRequired()])
    answer = StringField('Answer', validators=[DataRequired()])
    is_correct = BooleanField('Is Correct Answer')
    submit = SubmitField('Add Answer')


class MultipleAnswersForm(FlaskForm):
    answers = FieldList(FormField(InputAnswerForm), min_entries=4)
    submit = SubmitField('Add Answers')
