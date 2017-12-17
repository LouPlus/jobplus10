from flask import Blueprint, render_template, url_for, flash, redirect
from jobplus.forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user, login_required

front = Blueprint('front', __name__)


@front.route('/')
def index():
    return render_template('index.html')


@front.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('logout success', 'success')
    return redirect(url_for('.index'))


@front.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('register success', 'success')
        return redirect(url_for('.login'))
    return render_template('register.html', form=form)
