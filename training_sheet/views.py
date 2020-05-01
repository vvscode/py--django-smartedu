from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View

from training_sheet.forms import CourseForm
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


class CourseEditClassView(View):
    def get(self, request, course_id=None):
        course = None if course_id is None else get_object_or_404(Course, pk=course_id)
        return render(
            request,
            "training_sheet/course_form.html",
            context={"form": CourseForm(instance=course)},
        )

    def post(self, request, course_id=None):
        form = CourseForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data

            tags = form_data["tags"]
            del form_data["tags"]

            course_teachers = form_data["course_teachers"]
            del form_data["course_teachers"]

            course = (
                Course.objects.create()
                if course_id is None
                else get_object_or_404(Course, pk=course_id)
            )
            for key, value in form_data.items():
                setattr(course, key, value)

            course.tags.set(tags)
            course.course_teachers.set(course_teachers)
            course.save()
            return redirect("training_sheet.course", course.pk)

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class CourseDeleteClassView(View):
    def post(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        course.delete()
        return redirect("training_sheet.index")
