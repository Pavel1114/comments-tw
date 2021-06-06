from factory import Faker, Sequence
from factory.django import DjangoModelFactory


class PostFactory(DjangoModelFactory):
    title = Sequence(lambda n: f"post #{n}")
    text = Faker("paragraph", nb_sentences=10)

    class Meta:
        model = "blog.Post"
