from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Lawyer,Case, Customer
from django.views.generic.detail import DetailView
from django.db import models
import users
from .forms import CaseForm,MessageForm
import folium
from geopy.geocoders import Nominatim

# Create your views here.
def create_consultation(request):

    specialisations=['Criminal', 'Labour', 'Intellectual Property', 'Corporate']
    lawyers = Lawyer.objects.all()
    context={'specialisations':specialisations, 'lawyers':lawyers}
    return render(request,'consultations/create_consultation.html', context)

def mapCreator(request):
    geolocator = Nominatim(user_agent='consult')
    lawyers = Lawyer.objects.all()
    locationsDict={}
    for object in lawyers:
        if object.location:
            locate = geolocator.geocode(object.location)
            miniL = []
            miniL.extend([locate.latitude, locate.longitude])
            locationsDict[object.name]=miniL
    m = folium.Map()
    
    for i in locationsDict.keys():
        folium.Marker(location=[locationsDict[i][0], locationsDict[i][1]], popup=i).add_to(m)
    m = m._repr_html_()
    context={'map':m}
    return render(request, 'consultations/mapCreator.html', context)

def lawyer(request,lawyer_id):
    if request.method=='POST':
        caseForm = CaseForm(request.POST)
        if caseForm.is_valid():
            c_id = users.views.c_id
            new_case = caseForm.save(commit=False)
            new_case.lawyer = Lawyer.objects.get(id=lawyer_id)
            new_case.customer = Customer.objects.get(id=c_id)
            new_case.save()
            caseNo=0
            cases = Case.objects.all()
            for object in cases:
                if object.customer==new_case.customer:
                    caseNo=object.identity
            string = '/consult/case/'+str(caseNo)
            return redirect(string)
        else:
            return HttpResponse('nope')
    else:
        caseForm = CaseForm()
        customerName = users.views.u_name
        lawyername = Lawyer.objects.get(id=lawyer_id)
        rating = lawyername.rating
        context = {'lawyer_id':lawyer_id,'lawyername':lawyername.name,'rating':rating, 'customerName':customerName, 'form':caseForm}
        return render(request,'consultations/lawyer.html',context)

def case(request,case_no):
    if request.method == 'POST':
        messageform = MessageForm(request.POST)
        if messageform.is_valid():
            u_name = users.views.u_name
            new_message = messageform.save(commit=False)
            new_message.case_id = Case.objects.get(identity=case_no)
            new_message.date_added = models.DateTimeField(auto_now_add=True)
            new_message.sender_name = u_name
            new_message.save()
            return redirect('/consult/case/'+str(case_no))
    else:
        messageform = MessageForm()
    case = Case.objects.get(identity=case_no)
    messages = case.message_set.all().order_by('-date_added')
    context = {'messages':messages,'messageform':messageform,'case':case}
    return render(request,'consultations/case.html',context)

def clients(request,lawyer_id):
    lawyer = Lawyer.objects.get(id=lawyer_id)
    cases = lawyer.case_set.all()
    context = {'cases':cases}
    return render(request,'consultations/clients.html',context)