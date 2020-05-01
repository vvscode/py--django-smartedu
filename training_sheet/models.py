from django.db import models

# https://habr.com/ru/post/313764/#OneToOneField
from django.contrib.auth.models import User


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=250)
    about_description = models.TextField()

    def __str__(self):
        return f"Teacher #{self.job_title}"

    class Meta:
        pass


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Student"


class Tag(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return f"Tag #{self.title}"

    class Meta:
        pass


class Course(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    course_teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return f"Course #{self.title}"

    class Meta:
        pass


class Group(models.Model):
    group_name = models.CharField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    students = models.ManyToManyField(Student)
    group_teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return f"Group: {self.group_name}"

    class Meta:
        pass
