from django.db import models
# https://habr.com/ru/post/313764/#OneToOneField
from django.contrib.auth.models import User

class Teacher(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  job_title = models.CharField(max_length=300)
  about_description = models.TextField()

class Student(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  
class Tag(models.Model):
  title = models.CharField(max_length=200)
  slug = models.CharField(max_length=200)

class Course(models.Model):
  title = models.CharField(max_length=300)
  description = models.TextField()
  tags = models.ManyToManyField(Tag)
  course_teachers = models.ManyToManyField(Teacher)

class Group(models.Model):
  course = models.ForeignKey(Course, on_delete=models.PROTECT)
  students = models.ManyToManyField(Student)
  group_teachers = models.ManyToManyField(Teacher)
