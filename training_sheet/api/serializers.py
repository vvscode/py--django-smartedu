from rest_framework import serializers
from ..models import Course, Student, Teacher, Tag, Group, ApplicationForTraining


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class GroupIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id",)


class CourseSerializer(serializers.ModelSerializer):
    course_teachers = TeacherSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class ApplicationForTrainingSerializer(serializers.ModelSerializer):
    group = GroupIdSerializer()

    # DRF  выдает такую заглушку
    #     {
    #     "group": {},
    #     "comment": "",
    #     "user": null
    # }
    # Хотя обрабатывает
    #     {
    #     "group": 3,
    #     "comment": "some text"
    # }
    # Два вопроса:
    # 1. Как поправить сигнатуру для group?
    # 2. Как убрать user? он все равно перетирается

    class Meta:
        model = ApplicationForTraining
        fields = "__all__"
