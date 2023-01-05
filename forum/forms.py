from django import forms

from .models import SubForum, Topic, TopicResponse

class SubForumRegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(SubForumRegisterForm, self).__init__(*args, **kwargs)
    """
    The SubForum Register Form 

    """
    class Meta:
        model = SubForum
        fields = ['title', 'description', 'category', 'students']

    def save(self, commit=True):
        subforum = super().save(commit=False)
        subforum.creator = self.user
        subforum.is_active = True
        if commit:
            subforum.save()
        return subforum

class TopicRegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.subforum = SubForum.objects.get(pk=kwargs.pop('initial').pop('subforum'))
        super(TopicRegisterForm, self).__init__(*args, **kwargs)
    """
    The Topic Register Form 

    """
    class Meta:
        model = Topic
        fields = ['title', 'content']

    def save(self, commit=True):
        topic = super().save(commit=False)
        topic.creator = self.user
        topic.subforum = self.subforum
        topic.is_active = True
        if commit:
            topic.save()
        return topic

class TopicResponseRegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.topic = Topic.objects.get(pk=kwargs.pop('initial').pop('topic'))
        super(TopicResponseRegisterForm, self).__init__(*args, **kwargs)
    """
    The TopicResponse Register Form 

    """
    class Meta:
        model = TopicResponse
        fields = ['content']

    def save(self, commit=True):
        response = super().save(commit=False)
        response.creator = self.user
        response.topic = self.topic
        if commit:
            response.save()
        return response