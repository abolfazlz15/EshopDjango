from django.urls import path
from . import views


app_name = 'core'
urlpatterns = [
    path('contactus', views.contactUsView, name='contact-us')
]