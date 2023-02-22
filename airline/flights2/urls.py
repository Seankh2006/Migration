from django.contrib import admin
from django.urls import path
from flights2 import views

urlpatterns = [
    path('flights2/', views.index),
    path("Airport/", views.Airport),
    path("<int:flight_id>", views.Flight2),
    path("detail<int:flight_id>", views.flightdetails, name="flightdetails"),
]
