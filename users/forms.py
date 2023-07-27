from django import forms
from consult.models import Customer, Lawyer

class CustomerForm(forms.ModelForm):
    name=forms.CharField(max_length=200)
    class Meta():
        model=Customer
        fields=['name']
        
class LawyerForm(forms.ModelForm):
    name = forms.CharField(max_length=200)
    specialisation=forms.CharField(max_length=200)
    location = forms.CharField(max_length=200)
    class Meta():
        model=Lawyer
        fields=['name', 'specialisation', 'location']
        
class LawyerLogin(forms.Form):
    name=forms.CharField(max_length=200)