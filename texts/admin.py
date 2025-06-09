from django.contrib import admin

from texts.models import LocalTexts

@admin.register(LocalTexts)
class TextsAdmin(admin.ModelAdmin):
    list_display = ('key','text')
    search_fields = ('key','text')