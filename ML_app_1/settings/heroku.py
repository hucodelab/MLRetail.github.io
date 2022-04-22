import environ

from ML_app_1.settings.base import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env("SECRET KEY")

ALLOWED_HOST = env.list("ALLOWED_HOST")

DATABASE = {
    "default": env.db()
}