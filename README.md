How to reproduce
================

Prerequisites
-------------

- Python 3.8.10
- PostgreSQL 11.12

Steps
-----

- create/activate a virtualenv
- `pip install -r requirements.txt`
- tune `DATABASES` setting in `settings.py`
- `./manage.py migrate`
- `pip install django==3.2.6`
- uncomment `DEFAULT_AUTO_FIELD` in `settings.py`
- `./manage.py makemigrations`
- `./manage.py migrate`
