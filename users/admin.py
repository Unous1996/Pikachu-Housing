from django.contrib import admin

from users.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department',)


admin.site.register(UserProfile, UserProfileAdmin)
