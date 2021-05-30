from django.db.models import CharField, TextField
from django_extensions.db.models import TimeStampedModel


class Post(TimeStampedModel):
    title = CharField("название", max_length=500)
    text = TextField("текст")

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
        ordering = ("-created",)

    def __str__(self):
        return self.title
