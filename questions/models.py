from django.db import models
from consult.models import Lawyer,Customer
# Create your models here.

class Question(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)
    question = models.TextField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)


class Answer(models.Model):
    def __str__(self):
        return self.answer[:50]
    answer = models.TextField()
    lawyer = models.ForeignKey(Lawyer,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)