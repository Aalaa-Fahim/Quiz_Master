from flask import render_template, url_for, redirect, flash, request
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, UpdateForm
from app.models import User
from flask_login import login_required , login_user, logout_user, current_user
import os
import uuid

@app.route('/')
@app.route('/home')
def home():
  return render_template('index.html')


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
      flash('Login Successfully. Welcome.', 'success')
      get_next_page = request.args.get('next')
      if get_next_page:
        return redirect(get_next_page)
      else:
        return redirect(url_for('home'))
    else:
      flash('Login Failed. Please check email and password', 'danger')
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
    flash(f'{form.username.data} Account Created Successfully.You can login', 'success')
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

