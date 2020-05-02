from django.urls import path

from . import views

urlpatterns = [
    path("", views.CoursesListClassView.as_view(), name="training_sheet.index"),
    path(
        "course/add/",
        views.CourseCreateView.as_view(),
        name="training_sheet.course_add",
    ),
    path(
        "course/<int:pk>/",
        views.CourseClassView.as_view(),
        name="training_sheet.course",
    ),
    path(
        "course/edit/<int:pk>/",
        views.CourseEditView.as_view(),
        name="training_sheet.course_edit",
    ),
    path(
        "course/delete/<int:pk>/",
        views.CourseDeleteClassView.as_view(),
        name="training_sheet.course_delete",
    ),
]
