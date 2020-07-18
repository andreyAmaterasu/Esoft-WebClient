from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views
from .views import ManagerViewSet

router = DefaultRouter()
router.register("managers", ManagerViewSet)

urlpatterns = [
    path('tasks', views.tasks, name='tasks'),
    path('performers', views.performers, name='performers'),
    path('managers', views.managers, name='managers'),
]

urlpatterns += router.urls