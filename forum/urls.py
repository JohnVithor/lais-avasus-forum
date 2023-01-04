# forum/urls.py
from django.urls import path

from .views import SubForumDetailView, TopicDetailView, SubForumFormCreateView, SubForumFormEditView


urlpatterns = [
    path('subforum/', SubForumFormCreateView.as_view(), name="subforum-create-form"),
    path('subforum/<int:pk>', SubForumDetailView.as_view(), name="subforum-detail"),
    path('subforum/<int:pk>/edit', SubForumFormEditView.as_view(), name="subforum-edit-form"),
    path('topic/<int:pk>', TopicDetailView.as_view(), name="topic-detail")
]