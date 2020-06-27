from rest_framework import viewsets
from ..models import Course, Tag, Student
from .serializers import CourseSerializer, TagSerializer, StudentSerializer
from rest_framework.permissions import IsAuthenticated


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
