from django.contrib import admin
from .models import SubscribedUser


class SubscribedUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'subscription_date')


admin.site.register(SubscribedUser, SubscribedUserAdmin)
