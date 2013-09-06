#!/bin/sh
exec 2>&1

cd {{ ROOT }}
exec chpst -u {{ RUNIT_USER }}:{{ RUNIT_USER }} ENV=config/prod.py ./main.py
