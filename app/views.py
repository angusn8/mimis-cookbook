from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from .models import Profile, Recipe
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
    return render_template('search.html', user=current_user, recipes=Recipe.query.all())

@views.route('/profile')
@login_required
def profile():
    profile = Profile.query.filter_by(id=current_user.id).first()
    return render_template('profile.html', user=current_user, profile=profile, recipes=Recipe.query.filter_by(user_id=current_user.id).all())

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
        return redirect(url_for('views.profile', user=user, profile=profile, recipes=Recipe.query.filter_by(user_id=current_user.id).all()))
    return render_template('profile_settings.html', user=user, profile=profile)

@views.route('/recipe/upload', methods=['GET','POST'])
def recipe_upload():
    if request.method == 'POST':
        f = request.files['recipe_image']
        f.save(f'app/static/{f.filename}')
        user_id = current_user.id
        title = request.form.get('title')
        prep_time = request.form.get('prep_time')
        servings = request.form.get('servings')
        ingredients = request.form.get('ingredients')
        directions = request.form.get('directions')
        photo_path = f.filename
        print(photo_path)
        new_recipe = Recipe(user_id=user_id, username=current_user.username, title=title, time=prep_time, servings=servings, ingredients=ingredients, directions=directions, photo_path=photo_path)
        db.session.add(new_recipe)
        db.session.commit()
        profile = Profile.query.filter_by(id=current_user.id).first()
        return render_template("profile.html", user=current_user, profile=profile, recipes=Recipe.query.filter_by(user_id=current_user.id).all())
    return render_template('recipe_template.html')

@views.route('/recipe/view<int:recipe_id>', methods=['GET'])
def recipe_view(recipe_id):
    return render_template('recipes.html', user=current_user, recipe=Recipe.query.filter_by(id=recipe_id, user_id=current_user.id).first())

@views.route('/recipe/buy', methods=['GET'])
def recipe_buy():
    return render_template('others_recipes.html')