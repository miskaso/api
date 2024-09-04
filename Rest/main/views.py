from django.shortcuts import render
from rest_framework.response import Response

from .models import CarBrand, Book, Author, Profile, User
from rest_framework import generics
from .serializers import CarBrandSerializer, BookSerializer, AuthorSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets


# Create your views here.


class GetCarBrands(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class GetPostBook(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GetPostProfile(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer
