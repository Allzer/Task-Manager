from app import db


class Tasks(db.Model):

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.DateTime, nullable=False)