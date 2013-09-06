Flask-Peewee-Skeleton
=====================

Install
-------
    sudo pip install virtualenv fabric
    fab buildenv
    ./manage.py init
    sudo ./manage.py configure_nginx
    sudo ./manage.py configure_runit

Start server
------------
    ./main.py


Technology stack
----------------
- flask web framework
- gevent web server
- fabric
- runit supervisor
- nginx
- peewee sql orm
- flask-peewee extension with admin and rest api
- flask-script extension for django-like manage.py
- flask-debug-toolbar extension
