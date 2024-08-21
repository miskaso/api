from django.shortcuts import render
from .models import CarBrand
from rest_framework import generics
from .serializers import CarBrandSerializer

# Create your views here.


class GetCarBrands(generics.ListCreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class AllCars(generics.ListAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class GetOneCar(generics.RetrieveAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer