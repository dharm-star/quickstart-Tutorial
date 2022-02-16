from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .serializers import *
from rest_framework import viewsets ,permissions
# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permissions_class = [permissions.IsAuthenticated]

class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_class = [permissions.IsAuthenticated]