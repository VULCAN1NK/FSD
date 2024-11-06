from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_form, name='submit_form'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('entries/', views.view_entries, name='view_entries'),
]