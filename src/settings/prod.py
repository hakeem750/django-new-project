from base import *
from decouple import config



SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = ["ip-address", "www.domain.com"]
