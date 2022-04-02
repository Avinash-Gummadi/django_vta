from django.db import models
# Create your models here.
class UploadQuestion(models.Model):
    subjects = (('Programming','Programming'),('DBMS','DBMS'),('Oops','Oops'),('Python','Python'))
    optionsList = (('optionA','A'),('optionB','B'),('optionC','C'),('optionD','D'))
    subject = models.CharField(choices = subjects, max_length=100, blank=False)
    question = models.TextField(unique=False, blank=False)
    optionA = models.CharField(max_length=50, blank=False)
    optionB = models.CharField(max_length=50, blank=False)
    optionC = models.CharField(max_length=50, blank=False)
    optionD = models.CharField(max_length=50, blank=False)
    answer = models.CharField(choices = optionsList, max_length=50, blank=False)
