from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as generic_views
from rest_framework import generics as api_generic_views, permissions

from wakeapp.auth_app import forms
from wakeapp.auth_app import serializers as auth_serializers
from rest_framework.permissions import IsAuthenticated
UserModel = get_user_model()


class RegisterView(api_generic_views.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = auth_serializers.CreateUserSerializer
    permission_classes = (
        permissions.AllowAny,
    )


class LoginView:
    pass


class LogoutView:
    pass
