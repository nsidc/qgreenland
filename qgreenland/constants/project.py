import os

PROJECT = "QGreenland"
ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")
ENV_MANAGER = os.environ.get("QGREENLAND_ENV_MANAGER", "conda")

# In seconds. See
# https://2.python-requests.org/en/master/user/quickstart/#timeouts
REQUEST_TIMEOUT = 30

URS_COOKIE = "urs_user_already_logged"
