from django.urls import path, include
from rest_framework import routers

from .views import StudentViewSet, BookViewSet


router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'books', BookViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
]
