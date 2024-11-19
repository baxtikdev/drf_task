from .base import *
from .base import INSTALLED_APPS

# GENERAL
# ------------------------------------------------------------------------------

DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="lm38j75VInCWNiu09xTNBbFZSKdFIwUclj7JWriBFRKvDJAa0nBYOppcB6HowjkJ"
)

ALLOWED_HOSTS = ['*']

# EMAIL
# ------------------------------------------------------------------------------
# EMAIL_BACKEND = env("DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")
# or
EMAIL_HOST = env("EMAIL_HOST", default="mailpit")
EMAIL_PORT = 1025

# WhiteNoise
# ------------------------------------------------------------------------------
INSTALLED_APPS = ["whitenoise.runserver_nostatic", *INSTALLED_APPS]

# django-debug-toolbar
# ------------------------------------------------------------------------------

if DEBUG:
    INSTALLED_APPS += ["debug_toolbar"]
    DEBUG_TOOLBAR_CONFIG = {
        "DISABLE_PANELS": [
            "debug_toolbar.panels.redirects.RedirectsPanel",
            # Disable profiling panel due to an issue with Python 3.12:
            "debug_toolbar.panels.profiling.ProfilingPanel",
        ],
        "SHOW_TEMPLATE_CONTEXT": True,
    }
    INSTALLED_APPS += ["django_extensions"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
if env("USE_DOCKER") == "yes":
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

# Celery
# ------------------------------------------------------------------------------

CELERY_TASK_EAGER_PROPAGATES = True
# Your stuff...
# ------------------------------------------------------------------------------
