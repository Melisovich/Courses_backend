from rest_framework import serializers
from .models import CustomUser, UserProfile, Enrollment


class UserProfileSerializer(serializers.ModelSerializer):
    instructor_name = serializers.ReadOnlyField(source='user.first_name')

    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar', 'date_of_birth', 'created_at', 'updated_at', 'instructor_name']


class CustomUserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
