from flask import Flask, request, session


MESSAGE = """\
URL:        %s
Method:     %s
IP:         %s
User Agent: %s
Platform:   %s
Browser:    %s v.%s
User ID:    %s

"""

class LoggedFlask(Flask):
    def log_exception(self, exc_info):
        user_id = 'Not logged in'
        if session.get('logged_in'):
            user_id = session.get('user_pk')

        self.logger.error(MESSAGE % (
                request.url,
                request.method,
                request.remote_addr,
                request.user_agent.string,
                request.user_agent.platform,
                request.user_agent.browser,
                request.user_agent.version,
                user_id,
            ), exc_info=exc_info)
