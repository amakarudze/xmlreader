from django.urls import path

from . import views

app_name = "xmlreader"

urlpatterns = [path("", views.index, name="index")]
