# -*- coding: utf-8 -*-
'''
Production config. It may be overriden in config/local.py for development.
'''
from utils import from_root

DEBUG = False
BRAND = 'Flask Peewee Skeleton'

# nginx
IP = '0.0.0.0'
HOST = 'host.com'
PORT = 8000

# fabric
ENV_PATH = from_root('var/env')
REQUIREMENTS_FNAME = from_root('config/pip-req.txt')
DEPLOY_HOST = HOST
DEPLOY_PATH = '~/flask-peewee-skeleton'

# runit
RUNIT_USER = 'imbolc'
RUNIT_NAME = 'flask-peewee-skeleton'

ROOT = from_root('')
LOGGING = from_root('config/logging-prod.yaml')

SECRET_KEY = 'secret'

# flask-peewee
DATABASE = {
    'name': from_root('var/db.sqlite'),
    'engine': 'peewee.SqliteDatabase',
    'check_same_thread': False,
}

# debug toolbar
DEBUG_TB_PROFILER_ENABLED = True
DEBUG_TB_INTERCEPT_REDIRECTS = False
DEBUG_TB_PANELS = (
    'flask_debugtoolbar.panels.timer.TimerDebugPanel',
    'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
    'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
    'flask_debugtoolbar.panels.template.TemplateDebugPanel',
    'flask_debugtoolbar.panels.logger.LoggingPanel',
    'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
)


try:
    from local import *
except ImportError:
    pass
