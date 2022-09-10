from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(), max_length=1000)
    
    class Meta:
        model = Topic
        fields = ['subject', 'message']