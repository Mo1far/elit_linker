from flask import Flask, request, jsonify, redirect, abort

app = Flask(__name__)

DB = {}


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/link/', methods=['POST'])
def add_link():
    data = request.get_json()
    DB[data['slug']] = data['target_url']
    return jsonify({'status': 'ok'})


@app.route('/link/<string:slug>/', methods=['GET'])
def get_redirect(slug):
    url = DB.get(slug)
    if url is None:
        return jsonify({'description': 'Slug not found',
                        'status': 'error'}), 404
    return redirect(url)


if __name__ == '__main__':
    app.run()
