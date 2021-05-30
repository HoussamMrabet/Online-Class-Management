from django.db import models
from django import forms
from django.db.models.fields import NullBooleanField

# Create your models here.

<<<<<<< HEAD
class userApp(models.Model) :
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    Password =  models.CharField(max_length=50)
    Picture = models.ImageField(upload_to = 'pics')
    Roles = [
        ('s','Student'),
        ('t','Teacher'),
    ]
    Role = models.CharField(max_length=2,default='s',choices=Roles )

class classSubject (models.Model) :
    titleClass = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    codeClasse = models.IntegerField()
    creationDateClasse = models.DateField()


class course (models.Model) :
    desc = models.TextField(max_length=50)
    creationDateCourse =models.DateField()
    courseFile = models.FileField(null=True)
    course = models.ForeignKey(classSubject,on_delete=models.CASCADE)
    
class TD (models.Model) :
    titleTd = models.CharField(max_length=50)
    creationDateTd =models.DateField()
    tdFile = models.FileField(null=True)
    course = models.ForeignKey(classSubject,on_delete=models.CASCADE)

class TP (models.Model) :
    titleTp = models.CharField(max_length=50)
    creationDateTp =models.DateField()
    tpFile = models.FileField(null=True)
    course = models.ForeignKey(classSubject,on_delete=models.CASCADE)

class correction_TD_TP (models.Model) :
    title = models.CharField(max_length=50)
    creationDateTdTp =models.DateField()
    corrFile = models.FileField(null=True)
    course = models.ForeignKey(classSubject,on_delete=models.CASCADE)    

=======

class Users(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='profile_pics', blank=True)
    roles = [
        ('s', 'student'),
        ('t', 'teacher')
    ]
    role = models.CharField(
        max_length=2,
        choices=roles,
    )
>>>>>>> 83f27afee888c4afde06d3493f85a085b76a5d2e
