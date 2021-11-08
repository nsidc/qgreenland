import os

PROJECT = 'QGreenland'
ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')

# In seconds. See
# https://2.python-requests.org/en/master/user/quickstart/#timeouts
REQUEST_TIMEOUT = 30

URS_COOKIE = 'urs_user_already_logged'
