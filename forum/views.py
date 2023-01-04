from rest_framework import viewsets, permissions
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .serializers import CategorySerializer, SubForumSerializer, TopicSerializer
from .models import Category, SubForum, Topic
from .forms import SubForumRegisterForm
from django.urls import reverse_lazy

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class SubForumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows subforuns to be viewed or edited.
    """
    queryset = SubForum.objects.all().order_by('id')
    serializer_class = SubForumSerializer
    permission_classes = [permissions.IsAuthenticated]

class TopicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows subforuns to be viewed or edited.
    """
    queryset = Topic.objects.all().order_by('id')
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticated]



class SubForumDetailView(DetailView):
    model = SubForum
    template_name = 'forum/subforum-detail.html'

class TopicDetailView(DetailView):
    model = Topic
    template_name = 'forum/topic-detail.html'

class SubForumFormCreateView(CreateView):
    model = SubForum
    form_class = SubForumRegisterForm
    template_name = 'forum/subforum-register.html'
    success_url = reverse_lazy("home")

    def get_form_kwargs(self):
       kwargs = super(SubForumFormCreateView, self).get_form_kwargs()
       kwargs.update({'user': self.request.user})
       return kwargs
    
class SubForumFormEditView(UpdateView):
    model = SubForum
    form_class = SubForumRegisterForm
    template_name = 'forum/subforum-register.html'
    success_url = reverse_lazy("home")

    def get_form_kwargs(self):
       kwargs = super(SubForumFormEditView, self).get_form_kwargs()
       kwargs.update({'user': self.request.user})
       return kwargs