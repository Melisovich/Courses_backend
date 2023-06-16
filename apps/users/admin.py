from django.contrib import admin
from .models import CustomUser, UserProfile, Enrollment


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar_preview', 'bio', 'date_of_birth', 'created_at', 'updated_at']
    readonly_fields = ['avatar_preview']

    def avatar_preview(self, obj):
        return obj.avatar.url if obj.avatar else ''

    avatar_preview.short_description = 'Avatar Preview'
    avatar_preview.allow_tags = True


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(CustomUser)
admin.site.register(Enrollment)
