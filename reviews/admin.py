from django.contrib import admin

# Register your models here.
from .models import Course,Professor,Available_Courses

from django.contrib import admin



class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields={"name_slug":("name",)}

admin.site.register(Course)
admin.site.register(Professor)
admin.site.register(Available_Courses,CourseAdmin)