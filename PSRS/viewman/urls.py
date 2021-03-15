from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import FileViewSet, TasksViewSet

router = DefaultRouter()
router.register(r'', FileViewSet)
router.register(r'task', TasksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]