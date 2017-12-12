from django.contrib import admin

# Register your models here.
from .models import Main, Page, Card, Calendar, Portfolio, Folio

class FoliosInline(admin.TabularInline):
    model = Portfolio.folios.through


class PortfolioAdmin(admin.ModelAdmin):
    inlines = [
        FoliosInline,
    ]
    exclude = ('folios',)

admin.site.register(Main)
admin.site.register(Page)
admin.site.register(Card)
admin.site.register(Calendar)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Folio)

