'''
Production config overrides
'''
from utils import from_root

DEBUG = False

LOGGING = from_root('config/logging-prod.yaml')
