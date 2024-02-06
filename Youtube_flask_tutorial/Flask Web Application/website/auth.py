from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])

def login():
   if request.method == 'POST':
      identifier = request.form.get("identifier")  # Assuming the form input name is 'identifier'.
      password = request.form.get("password")

      # Attempt to fetch the user by email or username.
      user = User.query.filter((User.email == identifier) | (User.username == identifier)).first()

      if user:
         # If a user is found, check the password.
         if check_password_hash(user.password, password):
            flash('Logged in successfully', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
         else:
            flash('Incorrect password, try again', category='error')
      else:
         flash('Email or username does not exist', category='error')

   return render_template("login.html", user=current_user)

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
   if request.method == "POST":
      email = request.form.get("email")
      countrycode = request.form.get("countrycode")
      phone = request.form.get("phone")
      username = request.form.get("username")
      password1 = request.form.get("password1")
      password2 = request.form.get("password2")

      user = User.query.filter(User.email == email).first()
      name = User.query.filter(User.username == username).first()

      if user:
         flash('Email already exists', category='error')
      elif name:
         flash('username already exists', category='error')


      elif len(email) < 5:
         flash("Email must be at least 5 characters", category="error")
      elif not phone.isnumeric():
         flash("Phone number must only contain numerical digits", category="error")
      elif len(username) < 5:
         flash("Username must be at least 5 characters", category="error")
      elif len(password1) < 7:
         flash("Password must be at least 7 characters", category="error")
      elif password2 != password1:
         flash("Passwords do not match", category="error")
      else:
         new_user = User(email=email, username=username, phone=phone, password=generate_password_hash(password1))
         db.session.add(new_user)
         db.session.commit()
         # login_user(user, remember=True)
         flash("Account created", category="success")
         login_user(new_user, remember=True)
         return redirect(url_for('views.home'))

   return render_template("sign-up.html", user=current_user)

@auth.route("/logout")
@login_required
def logout():
   logout_user()
   return redirect(url_for('auth.login'))
