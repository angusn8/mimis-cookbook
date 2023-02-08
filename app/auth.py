from flask import Blueprint, render_template, request, flash, url_for, redirect
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from flask_change_password import ChangePassword, ChangePasswordForm, SetPasswordForm

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.search', user=current_user))
            else:
                flash('Incorrect Password', category='error')
        else:
            flash('No account for this email', category='error')
    else:
        flash('Please enter a valid email address', category='error')
    return render_template(('login.html'), user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(username) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(
                password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.search'))

    return render_template("signup.html", user=current_user)


@auth.route('/changepassword', methods=["GET", "POST"])
@login_required
def user_password_change():
    newPassword = request.form.get('password1')
    if request.method == 'POST':
        if request.form.get('password1') == request.form.get('password2') and len(request.form.get('password1')) >= 7:
            db.session.query(User).filter_by(id=current_user.id).update(
                {User.password: generate_password_hash(newPassword)})
            db.session.commit()
            flash('Password has been updated', category='success')
            return redirect(url_for('views.dashboard'))
        else:
            flash('Please enter a valid password. Make sure they match',
                  category='error')
            return render_template('changepassword.html', user=current_user)
    else:
        return render_template('changepassword.html', user=current_user)