from rest_framework import serializers

from .models import Category, SubForum, Topic

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'is_active', 'created_at']
        ordering = ['-id']

class SubForumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubForum
        fields = ['title', 'description', 'category', 'creator', 'students', 'is_active', 'created_at', 'updated_at']
        ordering = ['-id']
        
class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ['title', 'content', 'subforum', 'creator', 'is_closed', 'is_active', 'created_at', 'updated_at']
        ordering = ['-id']