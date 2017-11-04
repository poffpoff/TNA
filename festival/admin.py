from django.contrib import admin

# Register your models here.
from .models import Main, Page, Link

admin.site.register(Main)
admin.site.register(Page)
admin.site.register(Link)

class FileAdmin(admin.ModelAdmin):
    list_display = ['fileLink']
    readonly_fields = ['fileLink']
