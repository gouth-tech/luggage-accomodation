from django.db import models
from django.utils.translation import ugettext_lazy as _
import sys
# Create your models here.


class LuggageType(models.Model):
    name = models.CharField(_('Name'), max_length=300, blank=True)
    cost = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Luggage Type"


class Luggage(models.Model):
    owner_name = models.CharField(_('Name'), max_length=300, blank=True)
    type = models.ManyToManyField('LuggageType', related_name="types")
    space_alloted = models.IntegerField()
    space_status = models.BooleanField(default=False)

    def __str__(self):
        return self.owner_name

    class Meta:
        verbose_name_plural = "Luggage"


class Booking(models.Model):
    customer_name = models.CharField(_('Name'), max_length=300, blank=True)
    owner_id = models.ForeignKey(Luggage, on_delete=models.CASCADE, related_name="luggage",)

    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name_plural = "Booking"