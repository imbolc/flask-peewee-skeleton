import logging
import gevent


logger = logging.getLogger('gevent')

class WSGIHandler(gevent.wsgi.WSGIHandler):
    def log_request(self, *args):
        '''Use standard logging'''
        message = self.format_request(*args)
        code = self.request.response_code
        if code < 404:
            logger.info(message)
        elif code < 500:
            logger.warn(message)
        else:
            logger.error(message)
