from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# Create your views here.


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = ["get", "head"]
