from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

router = DefaultRouter()
router.register("getperformers", views.PerformerViewSet)
router.register("getmanagers", views.ManagerViewSet)
router.register("gettasks", views.TaskViewSet)
router.register("performermanager", views.PerformerManagerViewSet)
router.register("taskperformermanager", views.TaskPerformerManagerViewSet)

urlpatterns = [
    path('tasks', views.tasks, name='tasks'),
    path('performers', views.performers, name='performers'),
]

urlpatterns += router.urls
