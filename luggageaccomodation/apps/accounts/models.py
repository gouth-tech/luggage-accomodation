from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token
from django.utils import timezone
from django.conf import settings

# Create your models here.


class User(AbstractUser):
    STATUS_CHOICES = (
        (1, _("Luggage Accomodator")),
        (2, _("Luggage Keeper")),
    )

    username = models.CharField(blank=True, max_length=20)
    email = models.EmailField(_('email address'), unique=True,
                              error_messages={'unique': 'A user with that email already exists.'},
                              blank=True
                              )
    password = models.CharField(_('password'), max_length=100, blank=True)
    user_type = models.IntegerField(choices=STATUS_CHOICES, default=1)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.first_name:
            return self.first_name + " " + self.last_name
        else:
            return self.email


class ExpiringToken(Token):

    class Meta(object):
        proxy = True

    def expired(self):
        now = timezone.now()
        return self.created < now - settings.EXPIRING_TOKEN_LIFESPAN
