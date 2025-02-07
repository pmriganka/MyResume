from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("index", views.index, name='home'),
    path("experience", views.experience, name='experience'),
    path("awards", views.awards, name='awards'),
    path("contact", views.contact, name='contact'),
]
