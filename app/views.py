from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from .models import Profile
from . import db
from fileinput import filename
from flask import *  

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/search')
@login_required
def search():
    return render_template('search.html', user=current_user)

@views.route('/profile')
@login_required
def profile():
    profile = Profile.query.filter_by(id=current_user.id).first()
    return render_template('profile.html', user=current_user, profile=profile)

@views.route('/profile/update', methods=['GET','POST'])
@login_required
def update_profile():
    profile = Profile.query.filter_by(id=current_user.id).first()
    user = current_user
    full_name = request.form.get('full_name')
    username = request.form.get('username')
    email = request.form.get('email')
    bio = request.form.get('bio')

    if request.method == 'POST':
        user.full_name = full_name
        user.username = username
        user.email = email
        profile.bio = bio

        db.session.commit()
        return redirect(url_for('views.profile', user=user, profile=profile))
    return render_template('profile_settings.html', user=user, profile=profile)

@views.route('/profile/upload')
@login_required
def upload_recipe():
    return render_template('recipe_template.html')
    
@views.route('/profile', methods=['POST'])  
def submit_form():  
    if request.method == 'POST':  
        f = request.files['recipe_image']
        f.save(f.filename)
        return render_template("profile.html", user=current_user, profile=profile, name=f.filename)  