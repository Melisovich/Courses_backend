from django.contrib import admin
from .models import Category, Course, Lesson, Review

admin.site.register(Category)
admin.site.register(Lesson)
admin.site.register(Review)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'instructor', 'created_at', 'updated_at')
    list_filter = ('category', 'instructor')
    search_fields = ('title', 'instructor__user__username')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Course, CourseAdmin)
