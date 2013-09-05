#!var/env/bin/python
from gevent import monkey; monkey.patch_all()
from gevent.wsgi import WSGIServer

from utils._gevent import WSGIHandler
from app import app
from auth import *
from admin import admin
from api import api
from models import *
from views import *


admin.setup()
api.setup()

server = WSGIServer(('', app.config['PORT']), app,
        handler_class=WSGIHandler)

if app.debug:
    from werkzeug import serving
    serving.run_with_reloader(server.serve_forever)
else:
    server.serve_forever()
