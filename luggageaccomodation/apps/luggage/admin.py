from django.contrib import admin

# Register your models here.
from .models import Luggage, LuggageType, Booking

admin.site.register(Luggage)
admin.site.register(LuggageType)
admin.site.register(Booking)
