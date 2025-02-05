from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import DateTime

db = SQLAlchemy()

class Eval(db.Model):
    __tablename__ = 'evals'  

    id = db.Column(db.Integer, primary_key=True)
    isMovie = db.Column(db.Boolean, default=False)
    isYT = db.Column(db.Boolean, default=False)
    isBook = db.Column(db.Boolean, default=False)
    isOther = db.Column(db.Boolean, default=False)
    types = db.Column(db.String(100))

    title = db.Column(db.String(100))
    description = db.Column(db.Text)

    reflect = db.Column(db.String(255))
    love = db.Column(db.String(255))
    hate = db.Column(db.String(255))
    lesson = db.Column(db.String(255))

    insights = db.Column(db.String(255))
    changes = db.Column(db.String(255))

    date_created = db.Column(db.DateTime(timezone=True), default=func.now())


