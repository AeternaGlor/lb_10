from rest_framework import serializers

from .models import Category, IceCream, Wrapper


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class IceCreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = IceCream
        fields = "__all__"


class WrapperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wrapper
        fields = "__all__"