from django.contrib import admin

# Register your models here.
from .models import Main, Page, Card, Calendar, Portfolio, Folio

class FolioInline(admin.TabularInline):
    model = Folio

class PortfolioAdmin(admin.ModelAdmin):
    inlines = [
        FolioInline,
    ]

admin.site.register(Main)
admin.site.register(Page)
admin.site.register(Card)
admin.site.register(Calendar)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Folio)

