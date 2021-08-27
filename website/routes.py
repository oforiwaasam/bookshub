from flask import Blueprint, render_template, flash, url_for, redirect
from flask_login import login_required, logout_user 

main = Blueprint('main', __name__)

# anyone who visits this page will see page
@main.route('/', methods=['GET', 'POST'])
def index():
  
  #### Return a rendered index.html file
  return render_template("index.html")

# You will also add route for adding notes here

# user cannot access this route unless their logged in
@main.route('/logout')
@login_required
def logout():
  logout_user()
  flash("You've been logged out", 'success')
  #### Return a rendered login.html file
  return redirect(url_for('auth.login'))