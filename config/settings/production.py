from .base import *  # noqa
from .base import BASE_DIR, MIDDLEWARE

STATIC_ROOT = BASE_DIR / "staticfiles"
MIDDLEWARE.insert(2, "whitenoise.middleware.WhiteNoiseMiddleware")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
