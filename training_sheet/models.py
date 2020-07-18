# https://habr.com/ru/post/313764/#OneToOneField

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


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
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=250)
    about_description = models.TextField()


class Student(AbstractModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


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


class ApplicationForTraining(AbstractModel):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField()
