from rest_framework.serializers import ModelSerializer

from apps.comments.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "created",
            "modified",
            "parent",
            "text",
            "entity_type",
            "entity_id",
            "level",
            "tree_id",
        )
