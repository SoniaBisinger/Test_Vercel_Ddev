from django.urls import path

from members.views import index


urlpatterns = [
    path('', index),
]
