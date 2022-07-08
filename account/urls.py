from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('register', views.registerView, name='register'),
    path('logout', views.logoutView, name='logout'),
]
