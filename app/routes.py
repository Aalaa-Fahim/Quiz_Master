from flask import render_template, url_for, redirect, flash, request
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, UpdateForm, QuizSelectCatForm, QuizForm, InputQuestionForm, InputAnswerForm, MultipleAnswersForm
from app.models import User, Quiz, Question, Answer, QuizResult, InputQuestion, InputAnswer
from flask_login import login_required , login_user, logout_user, current_user
import os
import uuid

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html')


@app.route('/about')
def about():
  return render_template('about.html', title='About')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      login_user(user, remember=form.remember.data)
      flash('Login Successfully. Welcome!', 'success')
      get_next_page = request.args.get('next')
      if get_next_page:
        return redirect(get_next_page)
      else:
        return redirect(url_for('home'))
    else:
      flash('Login Failed. Please, check your email and/or password', 'danger')
  return render_template('login.html', title='Login', form=form, submitted=request.method == 'POST')

@app.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form = RegistrationForm()
  if form.validate_on_submit():
    pw_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    new_user = User(username=form.username.data, email=form.email.data, password=pw_hash)
    db.session.add(new_user)
    db.session.commit()
    flash(f'{form.username.data} Account Created Successfully. Now, You can login.', 'success')
    return redirect(url_for('login'))
  return render_template('register.html', title='Register', form=form, submitted=request.method == 'POST')

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
  form = UpdateForm()
  if form.validate_on_submit():
    if form.profile_pic.data: #to edit profile img
      unique_filename = str(uuid.uuid4())
      file_name, file_ext = os.path.splitext(form.profile_pic.data.filename)
      new_pic_name = unique_filename + file_ext
      new_pic_path = os.path.join(app.root_path, 'static/images', new_pic_name)
      form.profile_pic.data.save(new_pic_path)
      current_user.img = new_pic_name #end here and img size need to have restrict
    current_user.username = form.username.data
    current_user.email = form.email.data
    db.session.commit()
    flash('Account Updated Successfully', 'success')
    return redirect(url_for('account'))
  elif request.method == 'GET':
    form.username.data = current_user.username
    form.email.data = current_user.email
  img_path = f"images/{current_user.img}" # if change path to profile_pics modify this
  img = url_for('static', filename=img_path)
  return render_template('account.html', title='Account', form=form, img=img, submitted=request.method == 'POST')

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('home'))
""" Previous code
@app.route('/start_quiz', methods=['GET', 'POST'])
@login_required
def start_quiz():
    form = QuizSelectCatForm()
    if form.validate_on_submit():
        selected_category = form.category.data
        quiz = Quiz.query.filter_by(category=selected_category).first()
        if quiz:
            return redirect(url_for('take_quiz', quiz_id=quiz.id))
        else:
            flash('No quizzes are available in this category, yet.', 'warning')
    return render_template('start_quiz.html', title='Start Quiz', form=form, submitted=request.method == 'POST')

@app.route('/take_quiz/<int:quiz_id>', methods=['GET', 'POST'])
@login_required
def take_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = quiz.questions
    form = QuizForm()
    if request.method == 'POST':
        # Logic to calculate the score based on user's answers
        score = calculate_score(request.form, questions)
        quiz_result = QuizResult(user_id=current_user.id, quiz_id=quiz.id, score=score)
        db.session.add(quiz_result)
        db.session.commit()
        return redirect(url_for('view_score', quiz_result_id=quiz_result.id))
    return render_template('take_quiz.html', title='Take Quiz', quiz=quiz, questions=questions, form=form)

    
=> The new added code"""
@app.route('/start_quiz', methods=['GET', 'POST'])
@login_required
def start_quiz():
    return redirect(url_for('quiz_categories'))
"""
@app.route('/quiz_categories', methods=['GET', 'POST'])
@login_required
def quiz_categories():
    categories = ['History', 'Science', 'Programming']
    return render_template('quiz_categories.html', categories=categories)

@app.route('/quiz/<string:category>', methods=['GET', 'POST'])
@login_required
def quiz_category(category):
    quiz = Quiz.query.filter_by(category=category).first()
    if quiz:
        return redirect(url_for('take_quiz', quiz_id=quiz.id))
    else:
        flash('No quizzes are available in this category, yet.', 'warning')
        return redirect(url_for('quiz_categories'))

@app.route('/take_quiz/<string:category>', methods=['GET', 'POST'])
@login_required
def take_quiz(category):
    quizzes = Quiz.query.filter_by(category=category).all()
    if not quizzes:
        flash('No quizzes are available in this category yet.', 'warning')
        return redirect(url_for('quiz_categories'))
    quiz = quizzes[0]  # Assume we take the first quiz available in the category
    questions = quiz.questions
    form = QuizForm()
    if request.method == 'POST':
        score = calculate_score(request.form, questions)
        quiz_result = QuizResult(user_id=current_user.id, quiz_id=quiz.id, score=score)
        db.session.add(quiz_result)
        db.session.commit()
        return redirect(url_for('view_score', quiz_result_id=quiz_result.id))
    return render_template('take_quiz.html', title='Take Quiz', quiz=quiz, questions=questions, form=form)

@app.route('/view_score/<int:quiz_result_id>', methods=['GET'])
@login_required
def view_score(quiz_result_id):
    quiz_result = QuizResult.query.get_or_404(quiz_result_id)
    return render_template('view_score.html', title='Quiz Score', quiz_result=quiz_result)

def calculate_score(form_data, questions):
    score = 0
    for question in questions:
        selected_answer = form_data.get(f'question-{question.id}')
        if selected_answer:
            answer = Answer.query.get(int(selected_answer))
            if answer and answer.is_correct:
                score += 1
    return score
"""
@app.route('/add_question', methods=['GET', 'POST'])
@login_required
def add_question():
    form = InputQuestionForm()
    if form.validate_on_submit():
        new_question = InputQuestion(text=form.question.data, category=form.category.data)
        db.session.add(new_question)
        db.session.commit()
        flash('Question added successfully!', 'success')
        return redirect(url_for('add_answer', question_id=new_question.id))
    return render_template('add_question.html', title='Add Question', form=form)

@app.route('/add_answer', methods=['GET', 'POST'])
@login_required  # Ensure only logged-in users can add answers
def add_answer():
    question_id = request.args.get('question_id', type=int)
    if not question_id:
        flash('No question ID provided', 'danger')
        return redirect(url_for('index'))  # Redirect to index or appropriate page

    form = MultipleAnswersForm()

    # Pre-fill question_id for each answer form
    for answer_form in form.answers:
        answer_form.question_id.data = question_id

    if form.validate_on_submit():
        try:
            for answer_form in form.answers:
                answer_text = answer_form.answer.data
                is_correct = answer_form.is_correct.data

                # Create an instance of InputAnswer and add it to the session
                answer = InputAnswer(text=answer_text, is_correct=is_correct, question_id=question_id)
                db.session.add(answer)

            db.session.commit()
            flash('Answers added successfully!', 'success')
            return redirect(url_for('add_answer', question_id=question_id))

        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {e}', 'danger')

    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')

    return render_template('add_answer.html', form=form, question_id=question_id)


"""last try code"""

@app.route('/quiz_categories', methods=['GET', 'POST'])
@login_required
def quiz_categories():
    form = QuizSelectCatForm()
    if form.validate_on_submit():
        category = form.category.data
        return redirect(url_for('quiz', category=category))  # Pass selected category to quiz route
    return render_template('quiz_categories.html', form=form)
"""
@app.route('/quiz/<category>', methods=['GET', 'POST'])
@login_required
def quiz(category):
    quiz = Quiz.query.filter_by(category=category).first()
    if not quiz:
        flash(f'No quizzes available for {category}.', 'warning')
        return redirect(url_for('quiz_categories'))
    form = QuizForm()
    if request.method == 'POST':
        score = calculate_score(request.form, quiz.questions)
        quiz_result = QuizResult(user_id=current_user.id, quiz_id=quiz.id, score=score)
        db.session.add(quiz_result)
        db.session.commit()
        return redirect(url_for('view_score', quiz_result_id=quiz_result.id))
    return render_template('quiz.html', title=f'{category.capitalize()} Quiz', quiz=quiz, questions=quiz.questions, form=form)
"""
@app.route('/quiz/<category>', methods=['GET', 'POST'])
@login_required
def quiz(category):
    quiz = Quiz.query.filter_by(category=category).first()  # Fetch quiz based on category
    if not quiz:
        flash(f'No quizzes available for the selected category.', 'warning')
        return redirect(url_for('quiz_categories'))

    form = QuizForm()
    if form.validate_on_submit():
        score = calculate_score(request.form, quiz.questions)
        quiz_result = QuizResult(user_id=current_user.id, quiz_id=quiz.id, score=score)
        db.session.add(quiz_result)
        db.session.commit()
        return redirect(url_for('view_score', quiz_result_id=quiz_result.id))

    return render_template('quiz.html', title=f'{quiz.category.capitalize()} Quiz', quiz=quiz, form=form)


@app.route('/view_score/<int:quiz_result_id>', methods=['GET'])
@login_required
def view_score(quiz_result_id):
    quiz_result = QuizResult.query.get_or_404(quiz_result_id)
    return render_template('view_score.html', title='Quiz Score', quiz_result=quiz_result)

def calculate_score(form_data, questions):
    score = 0
    for question in questions:
        selected_answer = form_data.get(f'question-{question.id}')
        if selected_answer:
            answer = Answer.query.get(int(selected_answer))
            if answer and answer.is_correct:
                score += 1
    return score
