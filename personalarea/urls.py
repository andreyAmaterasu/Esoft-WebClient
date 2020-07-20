from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

urlpatterns = [
    path('tasks', views.tasks, name='tasks'),
    path('performers', views.performers, name='performers'),
]
