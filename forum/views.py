from rest_framework import viewsets, permissions
from .serializers import CategorySerializer
from .models import Category
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]