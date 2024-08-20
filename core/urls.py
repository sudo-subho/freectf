from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
    path('room2/', views.room2, name="room2"),
    path('room3/', views.room3, name="room3"),
    path('room4/', views.room4, name="room4"),
]
