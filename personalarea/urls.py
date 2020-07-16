from django.urls import path
from . import views

urlpatterns = [
    path('tasks', views.tasks, name='tasks'),
    path('performers', views.performers, name='performers'),
    path('managers', views.managers, name='managers'),
]