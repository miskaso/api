from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'cars', views.GetCarBrands)
router.register(r'books', views.GetPostBook, basename='books')

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', views.GetPostProfile.as_view(), name='profile'),
    path('api/token/', TokenObtainPairView.as_view(), name='obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
]
