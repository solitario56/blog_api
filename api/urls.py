from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, ComentarioViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
