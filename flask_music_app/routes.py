from flask import Blueprint, request, jsonify
from models import db, Artist, Music

artist_routes = Blueprint('artist_routes', __name__)
music_routes = Blueprint('music_routes', __name__)

# Artist CRUD Routes
@artist_routes.route('/artists', methods=['GET'])
def get_artists():
    artists = Artist.query.all()
    return jsonify([{'id': artist.id, 'name': artist.name, 'genre': artist.genre} for artist in artists])

@artist_routes.route('/artist', methods=['POST'])
def add_artist():
    data = request.json
    new_artist = Artist(name=data['name'], genre=data.get('genre', ''))
    db.session.add(new_artist)
    db.session.commit()
    return jsonify({'message': 'Artist created successfully'}), 201

@artist_routes.route('/artist/<int:id>', methods=['PUT'])
def update_artist(id):
    artist = Artist.query.get(id)
    if not artist:
        return jsonify({'message': 'Artist not found'}), 404
    data = request.json
    artist.name = data['name']
    artist.genre = data.get('genre', artist.genre)
    db.session.commit()
    return jsonify({'message': 'Artist updated successfully'})

@artist_routes.route('/artist/<int:id>', methods=['DELETE'])
def delete_artist(id):
    artist = Artist.query.get(id)
    if not artist:
        return jsonify({'message': 'Artist not found'}), 404
    db.session.delete(artist)
    db.session.commit()
    return jsonify({'message': 'Artist deleted successfully'})

# Music CRUD Routes
@music_routes.route('/music', methods=['GET'])
def get_music():
    music_list = Music.query.all()
    return jsonify([{'id': music.id, 'title': music.title, 'album': music.album, 'artist_id': music.artist_id} for music in music_list])

@music_routes.route('/music', methods=['POST'])
def add_music():
    data = request.json
    new_music = Music(title=data['title'], album=data.get('album', ''), artist_id=data['artist_id'])
    db.session.add(new_music)
    db.session.commit()
    return jsonify({'message': 'Music created successfully'}), 201

@music_routes.route('/music/<int:id>', methods=['PUT'])
def update_music(id):
    music = Music.query.get(id)
    if not music:
        return jsonify({'message': 'Music not found'}), 404
    data = request.json
    music.title = data['title']
    music.album = data.get('album', music.album)
    music.artist_id = data['artist_id']
    db.session.commit()
    return jsonify({'message': 'Music updated successfully'})

@music_routes.route('/music/<int:id>', methods=['DELETE'])
def delete_music(id):
    music = Music.query.get(id)
    if not music:
        return jsonify({'message': 'Music not found'}), 404
    db.session.delete(music)
    db.session.commit()
    return jsonify({'message': 'Music deleted successfully'})
