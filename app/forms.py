from django import forms # type: ignore
from app.models import *
class TopicModelForms(forms.ModelForm):
    class Meta:
        model = Topic
        fields ='__all__'

class WebpageModelForms(forms.ModelForm):
    class Meta:
        model = Webpage
        fields ='__all__'

class AccessRecordModelForms(forms.ModelForm):
    class Meta:
        model = AccessRecord
        fields ='__all__'
        
