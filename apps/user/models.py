from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from helpers.models import AbstractIdOnlyModel


class User(AbstractIdOnlyModel, AbstractUser):
    first_name = models.CharField(_('First Name'), max_length=50)
    last_name = models.CharField(_('Last Name'), max_length=50)
    email = models.EmailField(_('Email Address'), unique=True)
    is_active = models.BooleanField(
        _('Is Active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'
        ),
        db_index=True,
    )
