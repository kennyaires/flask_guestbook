from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .app import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    comment_text = db.Column(db.String(1000))

    def __repr__(self):
        return '<Comment {}>'.format(self.name) 
