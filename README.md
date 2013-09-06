Flask-Peewee-Skeleton
=====================

Install
-------
    sudo pip install virtualenv fabric
    fab buildenv
    ./manage.py init


Start development server
------------------------
    ./main.py


Start production server
-----------------------
    ENV=config/prod.py ./main.py


Install on production server
----------------------------
    sudo pip install virtualenv fabric
    fab buildenv
    ./manage.py init
    sudo ./manage.py configure_nginx



Technology stack
----------------
- flask web framework
- gevent web server
- fabric
- peewee sql orm
- flask-peewee extension with admin and rest api
- flask-script extension for django-like manage.py
- flask-debug-toolbar extension
