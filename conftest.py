from django.conf import settings
import os
import sys


def pytest_configure(config):
    os.environ['EXAMPLE_DIR'] = example_dir = os.path.normpath(
      os.path.join(os.path.dirname(__file__), 'example'))
    if example_dir not in sys.path:
        sys.path.insert(0, example_dir)
    if not settings.configured:
        os.environ['DJANGO_SETTINGS_MODULE'] = 'example.settings'

    test_db = os.environ.get('DB', 'sqlite')
    if test_db == 'mysql':
        settings.DATABASES['default'].update({
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'redrover',
          'USER': 'root'})
    elif test_db == 'postgres':
        settings.DATABASES['default'].update({
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'USER': 'postgres',
          'NAME': 'redrover',
          'OPTIONS': {'autocommit': True}})
    elif test_db == 'sqlite':
        settings.DATABASES['default'].update({
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': ':memory:'})
