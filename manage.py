#!var/env/bin/python
import os
import stat

from flask import render_template
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


def config_must_contain(*var_names):
    for var in var_names:
        assert var in app.config, 'You need to define config.%s' % var


@manager.command
def configure_nginx():
    config_must_contain('ROOT', 'HOST', 'IP', 'PORT')
    fname = '/etc/nginx/sites-enabled/%s' % app.config['HOST']
    config = render_template('config/nginx.txt', **app.config)
    print config
    if prompt_bool('Save this config to the %s' % fname):
        with open(fname, 'w') as f:
            f.write(config)
        print ('Saved. You can restart nginx with: \n\tsudo /etc/init.d/nginx '
                'configtest && sudo /etc/init.d/nginx restart')

@manager.command
def configure_runit():
    config_must_contain('ROOT', 'RUNIT_USER', 'RUNIT_NAME')
    fname = '/etc/service/%s/run' % app.config['RUNIT_NAME']
    config = render_template('config/runit.sh', **app.config)
    print config
    if prompt_bool('Save this config to the %s' % fname):
        try:
            os.makedirs(os.path.dirname(fname))
        except OSError:
            pass
        with open(fname, 'w') as f:
            f.write(config)
        st = os.stat(fname)
        os.chmod(fname, st.st_mode | stat.S_IEXEC)
        print 'Saved.'


if __name__ == "__main__":
    manager.run()
