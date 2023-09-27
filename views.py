from flask import Blueprint, render_template, request
from app import db  # Import the db object
from models.message import Message  # Import the Message model
from models.proposal import Proposal  # Import the Proposal model

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

        # Handle the proposal form submission
        user_answer = request.form.get("proposal_answer")
        
        if user_answer:
            new_proposal = Proposal(answer=user_answer)
            db.session.add(new_proposal)
            db.session.commit()

    return render_template("home.html", name="Snethemba")
