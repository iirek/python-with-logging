from flask import flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello'


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=9191)