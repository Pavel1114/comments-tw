import pytest


@pytest.mark.django_db
class TestCommentModel:
    def test_str(self, comment_factory):
        comment = comment_factory.create()
        assert str(comment) == f"комментарий #{comment.id}"

    def test_inheritance_parent_entity(self, comment_factory, post_factory):
        post = post_factory.create()
        parent_comment = comment_factory(entity=post)
        comment = comment_factory(parent=parent_comment)
        assert comment.entity == post
