import bjoern
from app import app

host = '0.0.0.0'
port = 5252

bjoern.run(app, host, port)