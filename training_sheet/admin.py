from django.contrib import admin

from .models import Teacher, Student, Tag, Course, Group

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Tag)
admin.site.register(Course)
admin.site.register(Group)