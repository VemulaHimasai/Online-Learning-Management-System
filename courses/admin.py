from django.contrib import admin
from .models import Course, Enrollment

# Register your models here.

# admin.site.register(Course)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher')
    search_fields = ('title',)
    list_filter = ('teacher',)

admin.site.register(Enrollment)