
from django.urls import path
from . import views

app_name = 'consult'

urlpatterns = [
    path('create_consultation',views.create_consultation,name='create_consultation'),
    path('lawyer/<int:lawyer_id>',views.lawyer,name='lawyer'),
    path('case/<int:case_no>',views.case,name='case'),
    path('<int:lawyer_id>/clients',views.clients,name='clients'),
]
