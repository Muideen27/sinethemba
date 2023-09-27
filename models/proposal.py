from app import db

class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(3), nullable=False)

    def __init__(self, answer):
        self.answer = answer
