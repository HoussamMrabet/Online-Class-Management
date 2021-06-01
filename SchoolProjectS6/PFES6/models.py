from django.db import models
from django import forms
from django.db.models.fields import NullBooleanField

# Create your models here.


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
        default='-'
    )


class classSubject (models.Model):
    titleClass = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    codeClasse = models.CharField(max_length=10)
    creationDateClasse = models.DateField()
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)


class JoinClass(models.Model):
    classId = models.ForeignKey(classSubject, on_delete=models.CASCADE)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)


class course (models.Model):
    desc = models.TextField(max_length=50)
    creationDateCourse = models.DateField()
    courseFile = models.FileField(upload_to='documents', null=True)
    course = models.ForeignKey(classSubject, on_delete=models.CASCADE)


class TD (models.Model):
    titleTd = models.CharField(max_length=50)
    creationDateTd = models.DateField()
    tdFile = models.FileField(upload_to='documents', null=True)
    course = models.ForeignKey(classSubject, on_delete=models.CASCADE)


class TP (models.Model):
    titleTp = models.CharField(max_length=50)
    creationDateTp = models.DateField()
    tpFile = models.FileField(upload_to='documents', null=True)
    course = models.ForeignKey(classSubject, on_delete=models.CASCADE)


class correction_TD_TP (models.Model):
    title = models.CharField(max_length=50)
    creationDateTdTp = models.DateField()
    corrFile = models.FileField(upload_to='documents', null=True)
    course = models.ForeignKey(classSubject, on_delete=models.CASCADE)


class Todo(models.Model):
    title = models.CharField(max_length=50)
    creationDateTodo = models.DateField()
    TodoTFile = models.FileField(upload_to='documents', null=True)
    TodoSFile = models.FileField(upload_to='documents', null=True)
    course = models.ForeignKey(classSubject, on_delete=models.CASCADE)
