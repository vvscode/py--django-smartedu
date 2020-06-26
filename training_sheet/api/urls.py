from django.urls import path
from . import views

app_name = "training_sheet"

urlpatterns = [
    path("courses/", views.CourseListView.as_view(), name="course_list"),
    path("courses/<pk>/", views.CourseDetailView.as_view(), name="course_details"),
    path("students/", views.StudentListView.as_view(), name="student_list"),
    path("tags/", views.TagListView.as_view(), name="tag_list"),
]
