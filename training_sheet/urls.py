from django.urls import path

from . import views

urlpatterns = [
    path("", views.CoursesListClassView.as_view(), name="training_sheet.index"),
    path(
        "course/<int:course_id>/",
        views.CourseClassView.as_view(),
        name="training_sheet.course",
    ),
]
