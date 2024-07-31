from django.urls import path

from . import views

app_name = "app_ndvi"

urlpatterns = [
    path("", views.Ndvi.as_view(), name="index"),
]