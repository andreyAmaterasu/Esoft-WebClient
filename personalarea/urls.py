from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

router = DefaultRouter()
router.register("getperformers", views.PerformerViewSet)
router.register("getmanagers", views.ManagerViewSet)
router.register("performermanager", views.PerformerManagerViewSet)
router.register("taskperformermanager", views.TaskPerformerManagerViewSet)
router.register("task", views.TaskViewSet)

urlpatterns = [
    path('tasks/task', views.task, name='task'),
    path('tasks', views.tasks, name='tasks'),
    path('performers', views.performers, name='performers'),
]

urlpatterns += router.urls
