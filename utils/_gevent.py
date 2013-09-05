import logging

import gevent
from werkzeug.http import HTTP_STATUS_CODES

from app import app


logger = logging.getLogger('gevent')

class WSGIHandler(gevent.wsgi.WSGIHandler):
    def log_request(self, *args):
        '''Use standard logging'''
        code = self.request.response_code
        if app.config['DEBUG']:
            message = '%s [%s: %s]' % (self.request.uri, code,
                    HTTP_STATUS_CODES.get(code, 'Unknown'))
        else:
            message = self.format_request(*args)
        if code < 404:
            logger.info(message)
        elif code < 500:
            logger.warn(message)
        else:
            logger.error(message)
