import pytest
from pytest_factoryboy import register

from apps.blog.tests.factories.post_factory import PostFactory
from apps.comments.tests.factories import CommentFactory

register(CommentFactory)
register(PostFactory)


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()
