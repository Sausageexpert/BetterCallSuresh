from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('',views.questions_home,name='questions_home' ),
    path('<int:question_id>',views.question,name='question'),
    ]
