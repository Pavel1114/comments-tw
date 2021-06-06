import pytest
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse

from apps.comments.models import Comment


@pytest.mark.django_db
class TestCommentsRetrieve:
    def test_retrieve(self, comment_factory, api_client):
        comment = comment_factory.create()
        res = api_client.get(reverse("comment-detail", kwargs={"pk": comment.pk}))
        assert res.status_code == 200

    def test_404(self, api_client):
        res = api_client.get("/comments/5/")
        assert res.status_code == 404


@pytest.mark.django_db
class TestCommentsCreate:
    @pytest.fixture
    def url(self):
        return reverse("comment-list")

    def test_with_empty_data(self, api_client, url):
        res = api_client.post(url)
        assert res.status_code == 400

    def test_with_valid_data(self, api_client, url, post_factory):
        post = post_factory()
        res = api_client.post(
            url,
            data={
                "text": "some text",
                "entity_id": post.id,
                "entity_type": ContentType.objects.get_for_model(post).id,
            },
        )
        assert res.status_code == 201
        assert Comment.objects.filter(id=res.json()["id"]).exists()


@pytest.mark.django_db
class TestCommentsList:
    @pytest.fixture
    def url(self):
        return reverse("comment-list")

    def test_list(self, api_client, comment_factory, url):
        comment_factory.create_batch(5)
        res = api_client.get(url)
        assert res.status_code == 200
        assert len(res.json()) == 5

    def test_filter_by_non_exists_comment_id(self, api_client, comment_factory, url):
        comment_factory.create_batch(10)
        res = api_client.get(f"{url}?comment_id=8")
        assert len(res.json()) == 0

    def test_filter_by_comment_id(self, api_client, comment_factory, url):
        comment_factory.create_batch(10)
        root = comment_factory()
        [second_level_comment, *_] = comment_factory.create_batch(3, parent=root)
        comment_factory.create_batch(3, parent=second_level_comment)  # third level
        res = api_client.get(f"{url}?comment_id={root.id}")
        assert len(res.json()) == 6  # 3 + 3
        res = api_client.get(f"{url}?comment_id={second_level_comment.id}")
        assert len(res.json()) == 3

    def test_filter_by_non_exists_entity(self, api_client, comment_factory, url):
        comment_factory.create_batch(10)
        res = api_client.get(f"{url}?entity_type=777&entity_id=777")
        assert len(res.json()) == 0

    def test_filter_by_entity(self, api_client, comment_factory, post_factory, url):
        post = post_factory()
        root = comment_factory(entity=post)
        comment_factory.create_batch(4, parent=root)
        res = api_client.get(f"{url}?entity_id={post.id}&entity_type={ContentType.objects.get_for_model(post).id}")
        assert len(res.json()) == 5
