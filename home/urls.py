from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('',views.index, name="home"),
    path('ravongla_star/', views.ravongla_star, name="ravongla_star"),
    path('contact/', views.contact,name="contact"),
    
]