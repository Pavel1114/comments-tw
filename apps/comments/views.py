from rest_framework.viewsets import ModelViewSet

from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer


class CommentsViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        query_params = self.request.query_params
        if "comment_id" in query_params:
            try:
                root = Comment.objects.get(id=int(query_params["comment_id"]))
                queryset = queryset.filter(tree_id=root.tree_id, level__gt=root.level)
            except Comment.DoesNotExist:
                queryset = Comment.objects.none()
        if "entity_type" in query_params:
            queryset = queryset.filter(
                entity_type_id=query_params["entity_type"],
            )
            if "entity_id" in query_params:
                queryset = queryset.filter(entity_id=query_params["entity_id"])
        return queryset
