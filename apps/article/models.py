from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.user.models import User
from helpers.models import AbstractBaseModel


class Article(AbstractBaseModel):
    author = models.ManyToManyField(User, verbose_name=_('Author'), related_name='articles', db_index=True)
    title = models.CharField(_('Title'), max_length=300, db_index=True)
    content = models.TextField(_('Content'))
    is_publish = models.BooleanField(_('Is Publish'), default=True)

    def __str__(self):
        return self.title

    @admin.display(description='authors')
    def get_author(self):
        return [user.username for user in self.author.all()]
