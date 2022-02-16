from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User, Group

class UsersSerializer(serializers.HyperlinkedModelSerializer): #(serializers.ModelSerializer): #(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields =['id', 'username', 'email', 'groups'] #"__all__"

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields =['id', 'name'] #"__all__"