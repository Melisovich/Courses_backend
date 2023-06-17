from django.contrib import admin
from .models import Category, Course, Lesson, Review


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'instructor', 'created_at', 'updated_at', 'rating']
    readonly_fields = ['rating']
    search_fields = ['title', 'category__name', 'instructor__user__email']
    list_filter = ['category', 'instructor']

    def rating(self, obj):
        return obj.calculate_rating()


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']
    search_fields = ['title', 'course__title']
    list_filter = ['course']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['course', 'user', 'created_at', 'rating']
    search_fields = ['course__title', 'user__user__email']
    list_filter = ['course', 'user']
    readonly_fields = ['course']

    def rating(self, obj):
        return obj.rating


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Review, ReviewAdmin)

