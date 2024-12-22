from django.shortcuts import render
from rest_framework import viewsets

from .models import Category, IceCream, Wrapper
from .serializers import CategorySerializer, IceCreamSerializer, WrapperSerializer


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    """
    The actions provided by the ModelViewSet class are
    .list(), .retrieve(), .create(), .update(), 
    .partial_update(), and .destroy()
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class IceCreamViewSet(viewsets.ModelViewSet):
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer


class WrapperViewSet(viewsets.ModelViewSet):
    queryset = Wrapper.objects.all()
    serializer_class = WrapperSerializer