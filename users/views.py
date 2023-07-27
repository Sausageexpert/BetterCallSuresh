from django.shortcuts import render, redirect
from .forms import CustomerForm, LawyerForm, LawyerLogin
from django.http import HttpRequest, HttpResponse
from consult.models import Lawyer, Customer

# Create your views here.

def customerRegister(request):
    global u_name
    global c_id
    if request.method=='POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            x = form.save()
            c_id = x.id
            u_name = Customer.objects.get(id=c_id).name
            return redirect('/consult/create_consultation')
        else:
            return HttpResponse('try again')
    else:  
        form=CustomerForm()
        return render(request, 'users/register1.html', {'form':form})

def lawyerRegister(request):
    global u_name
    if request.method=='POST':
        lawyerForm = LawyerForm(request.POST)
        if lawyerForm.is_valid():
            x = lawyerForm.save()
            '''lawyerName = lawyerForm.cleaned_data['name']'''
            l_id = x.id
            u_name = Lawyer.objects.get(id=l_id).name
            '''lawyers = Lawyer.objects.all()
            reqID=0
            for object in lawyers:
                if object.name==lawyerName:
                    reqID=object.id'''
            string='/consult/'+str(l_id)+'/clients'
            return redirect(string)
    else:
        form=LawyerForm()
        return render(request, 'users/register2.html', {'form':form})
    
def lawyerLogin(request):
    global l_id
    global u_name
    if request.method=='POST':
        
        lawyerForm=LawyerLogin(request.POST)
        lawyers = Lawyer.objects.all()
        if lawyerForm.is_valid():
            u_name = lawyerForm.cleaned_data['name']
        reqId=0
        for object in lawyers:
            if object.name==u_name:
                l_id = object.id
                reqId=object.id
                string='/consult/'+str(reqId)+'/clients'
                return redirect(string)
        else:
            return HttpResponse('nope')
    else:
        lawyerForm=LawyerLogin()
        return render(request, 'users/register3.html', {'form':lawyerForm})