from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import SQLAlchemy
from models import db, Artist, Music

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
db.init_app(app)
@app.before_first_request
def create_tables():
    db.create_all()
    