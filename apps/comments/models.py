from django.contrib.contenttypes.fields import GenericForeignKey
from django.db.models import CASCADE, ForeignKey, PositiveIntegerField, TextField
from django_extensions.db.models import TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey


class Comment(TimeStampedModel, MPTTModel):
    parent = TreeForeignKey("comments.Comment", on_delete=CASCADE, null=True, blank=True)
    text = TextField("текст")
    entity_type = ForeignKey("contenttypes.ContentType", on_delete=CASCADE, null=True, blank=True)
    entity_id = PositiveIntegerField(null=True, blank=True)
    entity = GenericForeignKey("entity_type", "entity_id")

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"
        ordering = ("-created",)

    def __str__(self):
        return f"комментарий #{self.pk}"

    def save(self, **kwargs):
        if self.parent:
            self.entity = self.parent.entity
        super().save(**kwargs)
