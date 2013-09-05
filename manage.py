#!var/env/bin/python
import os
from flask.ext.script import Manager, prompt, prompt_bool

from app import app
import models

MODELS = ['User', 'Relationship']

manager = Manager(app)


@manager.command
def init():
    syncdb()
    if app.config['SECRET_KEY'] == 'secret':
        print 'You mast change config.SECRET_KEY !'
        secretkey()


@manager.command
def syncdb():
    for m in MODELS:
        print '- create:', m
        getattr(models, m).create_table(fail_silently=True)
    if prompt_bool('Create admin?', default=True):
        createadmin()
    else:
        print 'You can do it later with: ./manage.py createadmin'


@manager.command
def dropdb():
    if not prompt_bool('Are you sure you want to lose all your data'):
        return
    for m in MODELS:
        print '- drop:', m
        getattr(models, m).drop_table(fail_silently=True)


@manager.command
def cleardb():
    dropdb()
    syncdb()


@manager.command
def createadmin():
    email = prompt('admin email', default='admin@admin.com')
    password = prompt('admin password', default='admin')
    admin = models.User(email=email, admin=True, active=True)
    admin.set_password(password)
    admin.save()


@manager.command
def secretkey():
    print 'Random secret key:', repr(os.urandom(24))


if __name__ == "__main__":
    manager.run()
