from django.contrib import admin

# Register your models here.
from .models import Main, Page, Card

admin.site.register(Main)
admin.site.register(Page)
admin.site.register(Card)

