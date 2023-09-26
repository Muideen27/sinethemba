from flask import Blueprint, render_template, request
from app import db  # Import the db object
from models.message import Message  # Import the Message model

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def home():
    # Your route logic here
    if request.method == "POST":
        user_message = request.form.get("user_message")

        if user_message:
            new_message = Message(text=user_message)
            db.session.add(new_message)
            db.session.commit()

    return render_template("home.html", name="Snethemba")
