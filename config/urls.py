from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.comments.views import CommentsViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("comments", CommentsViewSet)


urlpatterns = [
    path(settings.DJANGO_ADMIN_URL, admin.site.urls),
] + router.urls

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__", include(debug_toolbar.urls))]
