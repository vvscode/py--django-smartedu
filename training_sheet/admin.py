from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Teacher, Student, Tag, Course, Group, CustomUser

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Tag)
admin.site.register(Course)
admin.site.register(Group)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
