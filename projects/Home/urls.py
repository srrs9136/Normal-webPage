
from django import views
from django.contrib import admin
from django.urls import path,include

from django.urls import path
from .import views


urlpatterns = [

    path("1",views.Home_show),
    path("2",views.About_show),
    path("3",views.Info_show),
    path('Home',views.Homepress),
    path('',views.EnterPage)
  
]