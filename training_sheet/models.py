from django.db import models

# https://habr.com/ru/post/313764/#OneToOneField
from django.contrib.auth.models import User


class AbstractModel(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        data = [
            f"{key}={value!r}"
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        ]
        return f'{self.__class__.__name__}({", ".join(data)})'

    def __repr__(self):
        return str(self)


class Teacher(AbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=250)
    about_description = models.TextField()


class Student(AbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Tag(AbstractModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField()


class Course(AbstractModel):
    title = models.CharField(max_length=250)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    course_teachers = models.ManyToManyField(Teacher)


class Group(AbstractModel):
    group_name = models.CharField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    students = models.ManyToManyField(Student)
    group_teachers = models.ManyToManyField(Teacher)
