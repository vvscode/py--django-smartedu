from django.urls import path, include
from . import views

app_name = "training_sheet"

urlpatterns = [
    path(
        "courses/",
        views.CourseListView.as_view({"get": "list", "post": "create"}),
        name="course_list",
    ),
    path(
        "courses/<pk>/",
        views.CourseDetailView.as_view({"get": "list", "post": "create"}),
        name="course_details",
    ),
    path(
        "students/",
        views.StudentListView.as_view({"get": "list", "post": "create"}),
        name="student_list",
    ),
    path(
        "tags/",
        views.TagListView.as_view({"get": "list", "post": "create"}),
        name="tag_list",
    ),
    path("accounts/", include("rest_registration.api.urls")),
]
