# root/settings/local.py

from .base import *
from dotenv import load_dotenv

load_dotenv()

DEBUG = True
ALLOWED_HOSTS = []