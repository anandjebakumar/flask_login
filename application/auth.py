from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_user, current_user
from .forms import SignupForm, LoginForm
from .models import db, User
from . import login_manager

auth_bp = Blueprint(
    'auth_bp', 
    __name__, 
    template_folder='templates',
    static_folder='static'
)

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            print(next_page)
            return redirect(next_page or url_for('main_bp.dashboard'))
        return render_template('login.html',form=form,invalid_credentials=True)
    return render_template('login.html',form=form,invalid_credentials=False)

@auth_bp.route('/signup', methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(
                name = form.name.data,
                email = form.email.data,
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('main_bp.dashboard'))
        return render_template('signup.html',form=form,user_exists=True)
    return render_template('signup.html',form=form,user_exists=False)

@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None

@login_manager.unauthorized_handler
def unauthorized():
    print('You must be logged in to view that page')
    return redirect(url_for('auth_bp.login'))