from hashlib import md5
import datetime

import peewee as pw
from flask_peewee.auth import BaseUser

from app import db


class User(db.Model, BaseUser):
    email       = pw.CharField(unique=True)
    password    = pw.CharField()
    active      = pw.BooleanField(index=True, default=True)
    admin       = pw.BooleanField(default=False)
    joined      = pw.DateTimeField(index=True, default=datetime.datetime.now)

    @property
    def username(self):
        '''Hack for admin'''
        return self.email

    def __unicode__(self):
        return '%s <%s>' % (self.nickname, self.email)

    def following(self):
        return User.select().join(
            Relationship, on=Relationship.to_user
        ).where(Relationship.from_user==self).order_by(User.email)

    def followers(self):
        return User.select().join(
            Relationship, on=Relationship.from_user
        ).where(Relationship.to_user==self).order_by(User.email)

    def is_following(self, user):
        return Relationship.select().where(
            Relationship.from_user==self,
            Relationship.to_user==user
        ).exists()

    def gravatar_url(self, size=80):
        return 'http://www.gravatar.com/avatar/%s?d=identicon&s=%d' % \
            (md5(self.email.strip().lower().encode('utf-8')).hexdigest(), size)


class Relationship(db.Model):
    from_user   = pw.ForeignKeyField(User, related_name='relationships')
    to_user     = pw.ForeignKeyField(User, related_name='related_to')

    def __unicode__(self):
        return 'Relationship from %s to %s' % (self.from_user, self.to_user)
