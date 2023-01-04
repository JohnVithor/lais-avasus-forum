from django import forms
from datetime import date

from .models import SubForum

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

    # def clean(self):
    #     '''
    #     Add creator of subforum and activate it.
    #     '''
    #     cleaned_data = super().clean()
    #     cleaned_data["creator"] = self.user
    #     cleaned_data["is_active"] = True
    #     return cleaned_data

    def save(self, commit=True):
        subforum = super().save(commit=False)
        subforum.creator = self.user
        subforum.is_active = True
        if commit:
            subforum.save()
        return subforum