# root/settings/production.py

from .base import *

DEBUG = False

ALLOWED_HOSTS = ["your-ec2-public-ip"]

# security upgrades
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True