from django.urls import path
from . import views
from django.contrib import admin


admin.site.site_title = "Your info"
admin.site.site_header = "Info page"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit/', views.submit_form, name='submit_form'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('entries/', views.view_entries, name='view_entries'),
]