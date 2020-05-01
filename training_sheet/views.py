from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from django.views import View

from training_sheet.models import Course


class CoursesListClassView(View):
    def get(self, request):
        return render(
            request,
            "training_sheet/index.html",
            context={"courses": Course.objects.all()},
        )


class CourseClassView(View):
    def get(self, request, course_id):
        return render(
            request,
            "training_sheet/course.html",
            context={"course": get_object_or_404(Course, pk=course_id)},
        )
