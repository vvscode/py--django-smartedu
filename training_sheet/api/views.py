from rest_framework import viewsets, generics
from ..models import Course, Tag, Student, ApplicationForTraining, Group
from .serializers import (
    CourseSerializer,
    TagSerializer,
    StudentSerializer,
    ApplicationForTrainingSerializer,
    GroupSerializer,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.shortcuts import get_object_or_404


class CourseListView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class TagListView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class StudentListView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ApplicationForTrainingListAPIView(generics.ListCreateAPIView):
    queryset = ApplicationForTraining.objects.all()
    serializer_class = ApplicationForTrainingSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        request.data["user"] = self.request.user.pk
        super().create(request, *args, **kwargs)
