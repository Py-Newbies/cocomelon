from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# this is an example of Basic authentication
class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Students.objects.all()
    serializer_class = serializers.StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


# this is an example of open API i.e., no authentication
class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [IsAuthenticated]
