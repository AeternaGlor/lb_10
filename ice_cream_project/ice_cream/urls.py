from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, IceCreamViewSet, WrapperViewSet


router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'ice_cream', IceCreamViewSet, basename='ice_cream')
router.register(r'wrapper', WrapperViewSet, basename='wrapper')

urlpatterns = [
    path('', include(router.urls))
]
