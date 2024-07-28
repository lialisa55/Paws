from django.urls import path

from . import views

urlpatterns = [
        path("", views.vitrine, name="vitrine"),
]
