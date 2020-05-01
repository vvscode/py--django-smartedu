from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="training_sheet.index"),
    path("course/<int:course_id>/", views.course, name="training_sheet.course"),
]
