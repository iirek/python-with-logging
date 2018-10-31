import logging
from flask import Flask

log = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/hello')
def hello():
    log.info('Sample Message')
    return 'Hello'


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=9191)