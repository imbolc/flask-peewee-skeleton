# -*- coding: utf-8 -*-
from flask import Flask

from flask_peewee.db import Database
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config.from_object('config')
app.config.from_envvar('ENV', silent=True)

db = Database(app)

# extensions
DebugToolbarExtension(app)
