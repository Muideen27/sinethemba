from flask import Blueprint, render_template, request, flash, redirect, url_for
from app import db  # Import the db object
from models.message import Message  # Import the Message model
from models.proposal import Proposal  # Import the Proposal model
views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_message = request.form.get("user_message")
        print(f'Received message_answer: {user_message}')

        if user_message:
            new_message = Message(text=user_message)
            db.session.add(new_message)
            db.session.commit()

        # Debugging output to check the value of proposal_answer
        user_answer = request.form.get("proposal_answer")
        print(f"Received proposal_answer: {user_answer}")

        if user_answer:
            new_proposal = Proposal(answer=user_answer)
            db.session.add(new_proposal)
            db.session.commit()

    return render_template("home.html", name="Snethemba")
