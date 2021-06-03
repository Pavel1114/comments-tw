from .base import *  # noqa
from .base import INSTALLED_APPS, MIDDLEWARE


def show_toolbar(request):
    return True


MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
INSTALLED_APPS += ["debug_toolbar"]
DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": "config.settings.development.show_toolbar"}
