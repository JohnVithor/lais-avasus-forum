# users/views.py
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import StudentRegisterForm

from .models import CustomUser
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class SignUpView(generic.CreateView):
    form_class = StudentRegisterForm
    success_url = reverse_lazy("signup-success")
    template_name = "registration/signup.html"