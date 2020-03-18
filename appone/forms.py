from django import forms
from .models import Topic,Post
class topicform(forms.ModelForm):
    message=forms.CharField(
        widget=forms.Textarea( attrs={'placeholder':'what is on your mind?'}),max_length=4000)
    class Meta:
        model=Topic
        fields=['subject','message']

class postform(forms.ModelForm):
    class Meta:
        model=Post
        fields=['message']