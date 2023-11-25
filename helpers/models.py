import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractIdOnlyModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class AbstractBaseModel(AbstractIdOnlyModel):
    create_time = models.DateTimeField(_('Create Time'), auto_now_add=True)
    update_time = models.DateTimeField(_('Update Time'), auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-create_time',)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
