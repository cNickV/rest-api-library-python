from django.shortcuts import render
from rest_framework import viewsets
from .models import Library
from .serializers import LibrarySerializer

# Create your views here.


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    http_method_names = ["get", "head"]
