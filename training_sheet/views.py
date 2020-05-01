from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from training_sheet.models import Course


def index(request):
    return render(
        request, "training_sheet/index.html", context={"courses": Course.objects.all()}
    )


def course(request, course_id):
    return render(
        request,
        "training_sheet/course.html",
        context={"course": Course.objects.get(pk=course_id)},
    )
