from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import CustomUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['created_at', 'updated_at', 'is_active', 'cpf', 'name', 'social_name', 'birth_date', 'is_staff', 'state', 'city']
        ordering = ['-id']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        ordering = ['-id']