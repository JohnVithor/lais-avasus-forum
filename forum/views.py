from rest_framework import viewsets, permissions
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .serializers import CategorySerializer, SubForumSerializer, TopicSerializer
from .models import Category, SubForum, Topic, TopicResponse
from .forms import SubForumRegisterForm, TopicRegisterForm, TopicResponseRegisterForm
from django.urls import reverse_lazy
from django.shortcuts import redirect

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



class SubForumInfoView(DetailView):
    model = SubForum
    template_name = 'forum/subforum-detail.html'

class TopicInfoView(DetailView):
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

class TopicFormCreateView(CreateView):
    model = Topic
    form_class = TopicRegisterForm
    template_name = 'forum/topic-register.html'

    def get_initial(self):
        self.ctx = self.kwargs.copy()
        return self.kwargs

    def get_success_url(self):
        return reverse_lazy('topic-info',args=(self.object.pk,))

    def get_form_kwargs(self):
       kwargs = super(TopicFormCreateView, self).get_form_kwargs()
       kwargs.update({'user': self.request.user})
       return kwargs
    
    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['subforum'] = self.ctx['subforum']
        return context

class TopicResponseFormCreateView(CreateView):
    model = TopicResponse
    form_class = TopicResponseRegisterForm
    template_name = 'forum/topicresponse-register.html'

    def get_initial(self):
        self.ctx = self.kwargs.copy()
        return self.kwargs

    def get_success_url(self):
        return reverse_lazy('topic-info',args=(self.ctx['topic'],))

    def get_form_kwargs(self):
       kwargs = super(TopicResponseFormCreateView, self).get_form_kwargs()
       kwargs.update({'user': self.request.user})
       return kwargs
    
    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['topic'] = self.ctx['topic']
        return context

def close_topic(request, pk):
    if request.POST:
        topic = Topic.objects.get(id=pk)
        topic.is_closed = True
        topic.save()
        return redirect('topic-info', pk)

def open_topic(request, pk):
    if request.POST:
        topic = Topic.objects.get(id=pk)
        topic.is_closed = False
        topic.save()
        return redirect('topic-info', pk)
