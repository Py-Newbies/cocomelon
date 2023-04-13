from rest_framework import serializers
from . import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Students
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
