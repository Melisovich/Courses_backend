from rest_framework import serializers
from .models import Category, Course, Lesson, Review


class CategorySerializer(serializers.ModelSerializer):
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'category', 'instructor', 'created_at', 'updated_at', 'rating']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        review = Review.objects.create(**validated_data)
        course = review.course
        course.update_rating()
        return review

    class Meta:
        model = Review
        fields = ['id', 'course', 'user', 'comment', 'created_at', 'rating']

