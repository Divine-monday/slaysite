from django.urls import path
from . import views


urlpatterns = [
    path ('', views.home_view, name= "home"),
    path ('main/', views.main_view, name= "main"),
    path ('about/', views.about_view, name= "about"),
    path ('tour/', views.tour_view, name= "tour")
]