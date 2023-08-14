from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name="home"),
    path('weather/', views.weather_app, name="weather"),
]