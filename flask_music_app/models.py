from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50))
    
    # One-to-Many relationship with Music
    music = db.relationship('Music', backref='artist', lazy=True, cascade="all, delete")

class Music(db.Model):
    __tablename__ = 'music'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    album = db.Column(db.String(100))
    
    # Foreign Key for Artist
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
