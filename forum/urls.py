# forum/urls.py
from django.urls import path

from .views import SubForumDetailView, TopicDetailView


urlpatterns = [
    path('subforum/<int:pk>', SubForumDetailView.as_view(), name="subforum-detail"),
    path('topic/<int:pk>', TopicDetailView.as_view(), name="topic-detail")
]