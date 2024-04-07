from django.contrib import admin
from django.urls import include, path
from Car import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup.html', views.signup, name='signup'),
    path('register.html', views.register, name='register'),

]
