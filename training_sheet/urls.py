from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.CoursesListClassView.as_view(), name="training_sheet.index"),
    path(
        "soft_redirect",
        views.SoftRedirectView.as_view(),
        name="trainging_sheet.soft_redirect",
    ),
    path("contact_us", views.ContactUsView.as_view(), name="training_sheet.contact_us"),
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
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
]
