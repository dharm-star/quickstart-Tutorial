from django.contrib import admin

# Register your models here.
from simple_history import register
from django.contrib.auth.models import User

register(User)