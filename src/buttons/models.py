from app import db

class Buttons(db.Model):
    __tablename__ = 'buttons'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable=False)
