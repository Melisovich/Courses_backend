from django.urls import path
from .views import \
    CustomUserListCreateView,\
    CustomUserDetailView,\
    UserProfileListCreateView,\
    UserProfileDetailView

app_name = 'users-app'

urlpatterns = [
    path('users/', CustomUserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),
    path('profiles/', UserProfileListCreateView.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', UserProfileDetailView.as_view(), name='profile-detail'),
]
