from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/home")
def home():
    return render_template("home.html", name="Snethemba")