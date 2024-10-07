from flask import Flask
from models import db, Artist, Music
from routes import artist_routes, music_routes

app = Flask(__name__)

# Configuring SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Registering routes
app.register_blueprint(artist_routes)
app.register_blueprint(music_routes)

# Initialize DB
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
