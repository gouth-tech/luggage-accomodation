from django.urls import path
from .views import LuggageCreationAPIView, LuggageUpdateView, BookingCreationAPIView

app_name = 'apps.luggage'

urlpatterns = [

    path('luggage/luggage-creation/', LuggageCreationAPIView.as_view(), name="luggage-creation"),
    path('luggage/booking-creation/', BookingCreationAPIView.as_view(), name="booking-creation"),
    path('luggage/luggage-updation/', LuggageUpdateView.as_view(), name="luggage-updation"),

]
