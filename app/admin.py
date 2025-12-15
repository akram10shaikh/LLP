from django.contrib import admin
from .models import Section8

@admin.register(Section8)
class Section8Admin(admin.ModelAdmin):
    list_display = ('client_name', 'client_role', 'rating', 'display_order')
    list_editable = ('display_order',)
    search_fields = ('client_name', 'client_role')
    list_filter = ('rating',)

