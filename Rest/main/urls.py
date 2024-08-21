from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.GetCarBrands.as_view(), name='cars'),
    path('cars/all', views.AllCars.as_view(), name='all'),
    path('cars/<int:pk>/', views.GetOneCar.as_view(), name='one_car')
]
