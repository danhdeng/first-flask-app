from market import app
from flask import render_template, redirect, url_for
from market.models import Item, User
from market.forms import RegistrationForm, LoginForm
from market import db

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        print("validate start")
        user_to_create = User(username=form.username.data,
                              email=form.email.data,
                              password=form.password.data)
        print(user_to_create)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    return render_template('login.html', form=form)