import bjoern
from api import app

host = '0.0.0.0'
port = 5252

bjoern.run(app, host, port)