from django.db import models
from django.utils.translation import gettext_lazy as _

from helpers.models import AbstractBaseModel


class Category(AbstractBaseModel):
    name = models.CharField(_('Name'), max_length=100, db_index=True, unique=True)

    def __str__(self):
        return self.name
