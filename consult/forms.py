from django import forms
from .models import Case,Message

class CaseForm(forms.ModelForm):
    decs=forms.CharField(max_length=200)
    class Meta():
        model=Case
        fields=['decs']

class MessageForm(forms.ModelForm):
    message = forms.TextInput()
    class Meta():
        model=Message
        fields=['message']