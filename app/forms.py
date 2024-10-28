from django import forms # type: ignore
from app.models import *
class TopicModelForms(forms.ModelForm):
    class Meta:
        model = Topic
        fields ='__all__'

class WebpageModelForms(forms.ModelForm):
    class Meta:
        model = Webpage
        # fields ='__all__'
        # fields=['topic_name','name']
        exclude=['email']
        labels={'topic_name':'TN'}
        widgets={'url':forms.PasswordInput}
        help_texts={'topic_name':'This is parent data'}

class AccessRecordModelForms(forms.ModelForm):
    class Meta:
        model = AccessRecord
        fields ='__all__'
        # fields=['name','author']
        # exclude=['author']
        labels={'author':'A','date':'D','name':'N'}
        widgets={'date':forms.PasswordInput}
        help_texts={'name':'this is parent data'}

        
