from django.urls import include, path
from django.contrib import admin


api_urls = [

    path('', include('apps.luggage.urls')),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]
