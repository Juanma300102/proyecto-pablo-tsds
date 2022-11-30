from django.contrib import admin
from gestion.models import Student, Course


class StudentAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "surname", "dni", "birth", "adress", "course"]
    list_display_links = ["name", "surname"]


class CourseAdmin(admin.ModelAdmin):
    list_display = ["pk", "year", "divition"]


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
