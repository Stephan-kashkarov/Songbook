from app import app
from flask import render_template, redirect, url_for
from flask_login import current_user, login_user, login_required
from app.models import Person


@app.route("/")
def welcome():
	return render_template('main.html')


@app.route('/login')
def login():
	return "login"


@app.route('/register')
def register():
	return "register"


@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('welcome'))


@app.route('/home')
def home():
	return "home"


@app.route('/browse')
@login_required
def browse():
	return "browse"


@app.route('/about')
def about():
	return "about"
