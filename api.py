from flask_peewee.rest import (RestAPI, RestResource, UserAuthentication,
        AdminAuthentication, RestrictOwnerResource)

from app import app
from auth import auth
from models import User, Relationship


user_auth = UserAuthentication(auth)
admin_auth = AdminAuthentication(auth)

api = RestAPI(app, default_auth=user_auth)


class UserResource(RestResource):
    exclude = ('password', 'email',)


class RelationshipResource(RestrictOwnerResource):
    owner_field = 'from_user'
    include_resources = {
        'from_user': UserResource,
        'to_user': UserResource,
    }
    paginate_by = None


# register our models so they are exposed via /api/<model>/
api.register(User, UserResource, auth=admin_auth)
api.register(Relationship, RelationshipResource)
