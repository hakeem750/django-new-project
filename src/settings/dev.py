from .base import *
from decouple import config



SECRET_KEY = config("SECRET_KEY")
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]
