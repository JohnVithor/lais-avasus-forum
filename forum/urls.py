# forum/urls.py
from django.urls import path

from .views import *


urlpatterns = [
    path('subforum/', SubForumFormCreateView.as_view(), name="subforum-create-form"),
    path('subforum/<int:pk>', SubForumInfoView.as_view(), name="subforum-info"),
    path('subforum/<int:subforum>/new_topic', TopicFormCreateView.as_view(), name="topic-create-form"),
    path('subforum/<int:pk>/edit', SubForumFormEditView.as_view(), name="subforum-edit-form"),
    path('topic/<int:pk>', TopicInfoView.as_view(), name="topic-info"),
    path('topic/<int:topic>/new_response', TopicResponseFormCreateView.as_view(), name="response-create-form"),
    path('topic/<int:pk>/close', close_topic, name="topic-close"),
    path('topic/<int:pk>/open', open_topic, name="topic-open"),
]