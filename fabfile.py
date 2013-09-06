import os

from fabric import api
from fabric.context_managers import settings

import config

api.env.hosts = [config.DEPLOY_HOST]


def buildenv():
    try:
        os.makedirs(config.ENV_PATH)
    except OSError:
        pass
    with api.settings(warn_only=True):
        api.local('virtualenv %s' % config.ENV_PATH, capture=False)
    api.local('%s/bin/easy_install pip' % config.ENV_PATH, capture=False)
    api.local('%s/bin/pip install -r %s' % (
        config.ENV_PATH, config.REQUIREMENTS_FNAME), capture=False)


def upgrade(name):
    '''Upgrade library'''
    for line in open(config.REQUIREMENTS_FNAME):
        if name in line:
            api.local('%s/bin/pip install --upgrade --force %s' % (
                config.ENV_PATH, line.strip()))


def pull():
    api.local('git pull ssh://%s/%s' % (config.DEPLOY_HOST, config.DEPLOY_PATH))


def deploy_fix():
    api.local("git add -A && git commit -m'little fix'")
    api.local('fab deploy')


def deploy():
    push()
    with api.cd(config.DEPLOY_PATH):
        api.run('sudo sv restart %s' % config.RUNIT_NAME)


def push():
    with settings(warn_only=True):
        api.local('git push')
        api.local('git push ssh://%s/%s' % (config.DEPLOY_HOST, config.DEPLOY_PATH))


def log():
    with api.cd(config.DEPLOY_PATH):
        api.run('tail -n50 -f var/site.log')

