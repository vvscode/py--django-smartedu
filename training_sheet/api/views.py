from rest_framework import generics
from ..models import Course, Tag, Student
from .serializers import CourseSerializer, TagSerializer, StudentSerializer
from rest_framework.permissions import IsAuthenticated


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class StudentListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
