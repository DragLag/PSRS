from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import EggsViewSet

router = DefaultRouter()
router.register(r'', EggsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]