from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required, logout_user
from .models import db, User

main_bp = Blueprint(
    'main_bp',
    __name__, 
    template_folder='templates',
    static_folder='static'
)

@main_bp.route('/',methods=['GET'])
@login_required
def dashboard():
    return render_template('home.html',current_user=current_user)

@main_bp.route('/users',methods=['GET'])
@login_required
def users():
    users = User.query.all()
    return render_template('users.html',current_user=current_user,users=users)

@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))