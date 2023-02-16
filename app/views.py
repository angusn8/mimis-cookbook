from flask import Blueprint, render_template
from flask_login import current_user, login_required
from .models import Profile

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