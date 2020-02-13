from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TestViewSet

router = DefaultRouter()
router.register("test", TestViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
