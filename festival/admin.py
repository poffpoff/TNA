from django.contrib import admin

# Register your models here.
from .models import Main, Page, Card, Calendar, Portfolio, Folio

class FolioInline(admin.TabularInline):
    model = Folio

class PortfolioAdmin(admin.ModelAdmin):
    inlines = [
        FolioInline,
    ]

class CardesInline(admin.TabularInline):
    model = Card

class PagesInline(admin.TabularInline):
    model = Page

class MainAdmin(admin.ModelAdmin):
    inlines = [
        PagesInline,
        CardesInline
    ]

admin.site.register(Main, MainAdmin)
admin.site.register(Calendar)
admin.site.register(Portfolio, PortfolioAdmin)

