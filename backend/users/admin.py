from django.contrib import admin

from .models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    list_display = ["username", "email"]
