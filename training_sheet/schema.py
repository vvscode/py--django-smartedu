import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Course, Tag, Teacher, Group, Student, CustomUser

# https://webdevblog.ru/sozdanie-api-interfejsa-graphql-s-pomoshhju-django/


class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser


class CourseType(DjangoObjectType):
    class Meta:
        model = Course


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class GroupType(DjangoObjectType):
    class Meta:
        model = Group


class Query(ObjectType):
    customUsers = graphene.List(CustomUserType)
    courses = graphene.List(CourseType)
    teachers = graphene.List(TeacherType)
    tags = graphene.List(TagType)
    students = graphene.List(StudentType)
    groups = graphene.List(GroupType)

    def resolve_courses(self, info, **kwargs):
        return Course.objects.all()

    def resolve_teachers(self, info, **kwargs):
        return Teacher.objects.all()

    def resolve_tags(self, info, **kwargs):
        return Tag.objects.all()


class Mutation(ObjectType):
    pass


schema = graphene.Schema(query=Query)
