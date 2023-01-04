"""avasus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from rest_framework import routers

from users import views as user_views
from forum import views as forum_views

router = routers.DefaultRouter()
router.register(r'api/users', user_views.UserViewSet)
router.register(r'api/categories', forum_views.CategoryViewSet)
router.register(r'api/subforuns', forum_views.SubForumViewSet)
router.register(r'api/topics', forum_views.TopicViewSet)


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path("accounts/", include("users.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("forum/", include("forum.urls")),
    # path('users/', views.UserViewSet.as_view({'get': 'retrieve'})),
    # path('groups/', views.GroupViewSet.as_view({'get': 'retrieve'}))
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + router.urls
