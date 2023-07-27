from django.contrib import admin
from .models import Customer, Lawyer, Case, Message

# Register your models here.

admin.site.register(Customer)
admin.site.register(Lawyer)
admin.site.register(Case)
admin.site.register(Message)