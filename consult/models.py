from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Customer(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    
class Lawyer(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    CHOICES = (('Criminal', 'Criminal'), ('Labour', 'Labour'), ('Intellectual Property', 'Intellectual Property'), ('Corporate', 'Corporate'))
    specialisation = models.CharField(max_length=200, choices=CHOICES)
    rating = models.FloatField(default=3)
    no_of_ratings = models.IntegerField(default=0)
    location = models.CharField(max_length=200)
    
    
    
class Case(models.Model):
    def __str__(self):
        return str(self.identity)
    identity = models.AutoField(primary_key=True)
    decs = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    lawyer = models.ForeignKey(Lawyer, null=True, on_delete=models.PROTECT)
    location = models.CharField(max_length=200)


class Message(models.Model):
    def __str__(self):
        return str(self.case_id)
    case_id = models.ForeignKey(Case,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    sender_name = models.CharField(max_length=200)
    message = models.TextField()


