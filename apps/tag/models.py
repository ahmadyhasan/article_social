from helpers.models import AbstractBaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(AbstractBaseModel):
    slug = models.SlugField(_('Slug'), unique=True)

    def __str__(self):
        return self.slug
