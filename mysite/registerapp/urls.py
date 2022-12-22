from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUser, name='getUser'),
    path('post/',views.createUser,name='createUser'),
]