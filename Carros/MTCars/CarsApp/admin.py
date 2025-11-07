from django.contrib import admin
from django.urls import path
from CarsApp import views
from CarsApp.models import MTCars

app_name = "CarsApp"
admin.site.register(MTCars)


urlpatterns = [
    path("", views.searchf, name="home"),
]
