from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('users/', include(('apps.users.urls', 'users'), namespace='users-app')),
    path('jet/', include('jet.urls', 'jet')),
    path('', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('courses/', include('apps.courses.urls', namespace='courses')),
    path('users/', include('apps.users.urls', namespace='users')),
]
