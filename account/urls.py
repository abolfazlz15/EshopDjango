from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login', views.loginView, name='login'),
]