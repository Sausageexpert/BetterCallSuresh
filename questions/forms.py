from django import forms
from .models import Question,Answer

class AnswerForm(forms.ModelForm):
    answer = forms.TextInput()
    class Meta:
        model=Answer
        fields = ['answer']

class QuestionForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    question = forms.TextInput()
    class Meta:
        model=Question
        fields = ['title','question']