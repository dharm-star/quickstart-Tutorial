from rest_framework import routers
from django.urls import path, include
from quickstart import views

router = routers.DefaultRouter()
router.register(r'user',views.UserViewset,basename="users")
router.register(r'group',views.GroupViewset,basename="groups")

urlpatterns= [
    path('',include(router.urls)),
]