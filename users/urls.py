# users/urls.py
from django.urls import path

from .views import SignUpView, UserInfoView
from django.views.generic.base import TemplateView


urlpatterns = [
    path("signup-success/", TemplateView.as_view(template_name='registration/signup-success.html'), name='signup-success'),
    path("signup/", SignUpView.as_view(), name="signup-student"),
    path("user/<int:pk>", UserInfoView.as_view(), name="user-info")
]