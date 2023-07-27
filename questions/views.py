from django.shortcuts import render,redirect
from .models import Question,Answer
from .forms import AnswerForm,QuestionForm
from consult.models import Lawyer, Customer
import users

# Create your views here.
def questions_home(request):
    if request.method == 'POST':
        questionform = QuestionForm(request.POST)
        if questionform.is_valid():
            c_id = users.views.c_id
            new_question = questionform.save(commit=False)
            new_question.customer = Customer.objects.get(id=c_id)
            new_question.save()
            return redirect('/questions/')
    else:
        questionform = QuestionForm()

    questions = Question.objects.all()  
    context = {'questions':questions,'questionform':questionform}
    return render(request,'questions/questions_home.html',context)

def question(request,question_id):
    if request.method == 'POST':
        answerform = AnswerForm(request.POST)
        if answerform.is_valid():
            new_answer = answerform.save(commit=False)
            new_answer.question = Question.objects.get(id=question_id)
            new_answer.lawyer = Lawyer.objects.get(id=users.views.l_id)
            new_answer.save()
            return redirect('/questions/'+str(question_id))
    else:
        answerform = AnswerForm()
            
    question = Question.objects.get(id=question_id)
    answers = question.answer_set.all()
    context = {'question':question,'answers':answers,'answerform':answerform}
    return render(request,'questions/question.html',context)