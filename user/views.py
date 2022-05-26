from django.shortcuts import render
from rest_framework import viewsets
from .models import UserRequest
from .serializers import UserRequestSerializer

# Create your views here.


class UserRequestViewSet(viewsets.ModelViewSet):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer


class UserRequetsGetViewSet(viewsets.ModelViewSet):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer

    def get_queryset(self):
        userId = self.request.query_params.get("id")
        return UserRequest.objects.filter(user=userId)

    if queryset.count() > 2:
        http_method_names = ["get", "head"]


""" 
"admin/"
"api/shelf/"
"api/book/"
"api/users/"
"api/token/"
"api/token/refresh/"
"secure-page/"
"""
