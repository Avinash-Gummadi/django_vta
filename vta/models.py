from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_faculty = models.BooleanField(default=False)
    person_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)

class UploadQuestion(models.Model):
    subjects = (('programming','Programming'),('dbms','DBMS'),('oops','Oops'),('python','Python'))
    optionsList = (('A','A'),('B','B'),('C','C'),('D','D'))
    subject = models.CharField(choices = subjects, max_length=100, blank=False)
    question = models.TextField(unique=False, blank=False)
    optionA = models.CharField(max_length=50, blank=False)
    optionB = models.CharField(max_length=50, blank=False)
    optionC = models.CharField(max_length=50, blank=False)
    optionD = models.CharField(max_length=50, blank=False)
    answer = models.CharField(choices = optionsList, max_length=50, blank=False)
