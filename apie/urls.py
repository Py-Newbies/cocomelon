from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'products', views.ProductView)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
]
