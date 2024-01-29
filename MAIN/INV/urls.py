

from .views import indexView

from django.urls import path
urlpatterns = [
    path("", indexView, name="index"),
]