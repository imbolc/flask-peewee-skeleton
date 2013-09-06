# -*- coding: utf-8 -*-
'''
Development config. It may be overriden in config/prod.py for production.
'''
from utils import from_root

DEBUG = True
PORT = 8000
HOST = 'host.com'
IP = '0.0.0.0'
BRAND = 'Flask Peewee Skeleton'

# fabric
ENV_PATH = from_root('var/env')
REQUIREMENTS_FNAME = from_root('config/pip-req.txt')
DEPLOY_HOST = ''

LOGGING = from_root('config/logging-dev.yaml')

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
