from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.comments.models import Comment


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ("__str__", "parent", "entity", "entity_type")
