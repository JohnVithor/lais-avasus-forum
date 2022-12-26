from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer


from .models import CustomUser
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]