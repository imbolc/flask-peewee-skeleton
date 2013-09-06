# -*- coding: utf-8 -*-
import yaml
import logging.config

from flask_peewee.db import Database
from flask_debugtoolbar import DebugToolbarExtension

from utils._logging import LoggedFlask


app = LoggedFlask(__name__)
app.config.from_object('config')

# logging
logging.config.dictConfig(yaml.load(open(app.config['LOGGING'])))

# extensions
db = Database(app)
DebugToolbarExtension(app)
