"""Routes definitions"""
from flask import request, jsonify, redirect, Blueprint

index = Blueprint("index", __name__)

DB = {}


@index.route('/')
def hello_world():
    return 'Hello, World!'


@index.route('/link/', methods=['POST'])
def add_link():
    data = request.get_json()
    DB[data['slug']] = data['target_url']
    return jsonify({'status': 'ok'})


@index.route('/link/<string:slug>/', methods=['GET'])
def get_redirect(slug):
    url = DB.get(slug)
    if url is None:
        return jsonify({'description': 'Slug not found',
                        'status': 'error'}), 404
    return redirect(url)
