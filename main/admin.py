from django.contrib import admin

from main.models import GamingController

@admin.register(GamingController)
class GamingControllerAdmin(admin.ModelAdmin):
    list_display = ('year', 'title')
    search_fields = ('year', 'title')