from django.contrib import admin

# Register your models here.
from .models import Main, Page, Card, Portfolio, Folio, ThumbnailGallery, Thumbnail, Accordion, Key, GoogleMap, Index, FirstPage

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

class ThumbnailInline(admin.TabularInline):
    model = Thumbnail

class ThumbnailGalleryAdmin(admin.ModelAdmin):
    inlines = [
        ThumbnailInline,
    ]

class KeyInline(admin.TabularInline):
    model = Key

class AccordionAdmin(admin.ModelAdmin):
    inlines = [
        KeyInline,
    ]

class IndexInline(admin.TabularInline):
    model = Index

class FirstPageAdmin(admin.ModelAdmin):
    inlines = [
        IndexInline,
    ]

admin.site.register(Main, MainAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(ThumbnailGallery, ThumbnailGalleryAdmin)
admin.site.register(Accordion, AccordionAdmin)
admin.site.register(GoogleMap)
admin.site.register(FirstPage, FirstPageAdmin)

