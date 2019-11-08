from django.db import models
from django.utils.translation import ugettext_lazy as _
from apps.accounts.models import User
# Create your models here.


class LuggageType(models.Model):
    name = models.CharField(_('Name'), max_length=300, blank=True)
    cost = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Luggage Type"


class Luggage(models.Model):
    owner_name = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name="luggageaccomodator",
                                   blank=True, null=True)
    type = models.ManyToManyField('LuggageType', related_name="types")
    space_alloted = models.IntegerField()
    space_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Luggage"


class Booking(models.Model):
    customer_name = models.ForeignKey(User, on_delete=models.CASCADE,
                                      related_name="luggagekeeper",
                                      blank=True, null=True)
    owner_id = models.ForeignKey(Luggage, on_delete=models.CASCADE, related_name="luggage",)

    class Meta:
        verbose_name_plural = "Booking"