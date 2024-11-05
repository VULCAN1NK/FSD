from django.contrib import admin
from django.urls import path
from donor1 import views
urlpatterns = [
    
    path('boys/', views.donor , name="name")
]