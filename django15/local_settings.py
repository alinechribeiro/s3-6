from settings import PROJECT_ROOT, SITE_ROOT
import os

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "heroku_9d7b5325c374e89",
        "USER": "be16e7dcc4b577",
        "PASSWORD": "1d7faf72",
        "HOST": "us-cdbr-iron-east-04.cleardb.net",
        #"PORT": "5432",
    }
}
