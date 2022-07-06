from .base import *
from decouple import config

# Delete this placeholder and uncomment the comfig secret key for a reliable secret key
SECRET_KEY = "django-app-place-holder"
# SECRET_KEY = config("SECRET_KEY")
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]
