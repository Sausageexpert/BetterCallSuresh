from django.urls import path, include
from . import views

urlpatterns = [
    path('customerRegister/', views.customerRegister, name='customerRegister'),
    path('lawyerRegister/', views.lawyerRegister, name='lawyerRegister'),
    path('lawyerLogin/', views.lawyerLogin, name='lawyerLogin'),
]
