from rest_framework.viewsets import ModelViewSet

from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer


class CommentsViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
