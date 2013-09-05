from flask_peewee.auth import Auth as PeeweeAuth

from app import app, db
from models import User


class Auth(PeeweeAuth):
    def authenticate(self, username, password):
        active = self.User.select().where(self.User.active==True)
        try:
            user = active.where(self.User.email==username).get()
        except self.User.DoesNotExist:
            return False
        else:
            if not user.check_password(password):
                return False
        return user


auth = Auth(app, db, user_model=User)
