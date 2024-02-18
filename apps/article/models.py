from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.user.models import User
from apps.category.models import Category
from apps.tag.models import Tag
from helpers.models import AbstractBaseModel


class Article(AbstractBaseModel):
    tags = models.ManyToManyField(Tag, verbose_name=_('Tags'), related_name='articles', db_index=True)
    category = models.ManyToManyField(Category, verbose_name=_('Category'), related_name='articles', db_index=True)
    author = models.ManyToManyField(User, verbose_name=_('Author'), related_name='articles', db_index=True)
    title = models.CharField(_('Title'), max_length=300, db_index=True)
    content = models.TextField(_('Content'))
    is_publish = models.BooleanField(_('Is Publish'), default=True)

    def __str__(self):
        return self.title

    @admin.display(description='authors')
    def get_authors(self):
        return [user.username for user in self.author.all()]

    @admin.display(description='categories')
    def get_categories(self):
        return [category.name for category in self.category.all()]

    @admin.display(description='tags')
    def get_tags(self):
        return [tags.slug for tags in self.tags.all()]
