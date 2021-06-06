from django.contrib.contenttypes.models import ContentType
from factory import Faker, LazyAttribute, Maybe, SelfAttribute, SubFactory
from factory.django import DjangoModelFactory


class CommentFactory(DjangoModelFactory):
    text = Faker("paragraph", nb_sentences=10)
    parent = Maybe(
        "with_parent",
        no_declaration=None,
        yes_declaration=SubFactory("apps.comments.tests.factories.CommentFactory"),
    )
    entity_id = Maybe("entity", no_declaration=None, yes_declaration=SelfAttribute("entity.id"))
    entity_type = Maybe(
        "entity",
        no_declaration=None,
        yes_declaration=LazyAttribute(lambda o: ContentType.objects.get_for_model(o.entity)),
    )

    class Meta:
        model = "comments.Comment"
        exclude = ["with_parent"]
