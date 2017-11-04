from django.db import models
from colorfield.fields import ColorField
import os


# Create your models here.

class Page(models.Model):
    name = models.CharField(max_length=30)


class Link(models.Model):
    name = models.CharField(max_length=30)
    image = models.FileField('File', upload_to='./festival/userImages/')
    https = models.CharField(max_length=999)

    def fileLink(self):
        if self.File:
            return '<a href="' + str(self.File.url) + '">' + 'NameOfFileGoesHere' + '</a>'
        else:
            return '<a href="''"></a>'

    fileLink.allow_tags = True
    fileLink.short_description = "File Link"


class Main(models.Model):
    name = models.CharField(max_length=30)
    video_link = models.URLField()
    links = models.ManyToManyField(Link)
    pages = models.ManyToManyField(Page)

    background_color_up = ColorField(default='#000000')
    use_of_image_background_up = models.BooleanField(default=False)
    background_image_up = models.FileField('File', upload_to='./festival/userImages/')

    background_color_down = ColorField(default='#FFFFFF')
    use_of_image_background_down = models.BooleanField(default=False)
    background_image_down = models.FileField('File', upload_to='./festival/userImages/')

    font_style_navigation_bar = models.CharField( max_length =50, default='Crimson Text')
    font_size_navigation_bar = models.IntegerField(default='22')
    foreground_color_navigation_bar = ColorField(default='#FFFFFF')
    background_color_navigation_bar = ColorField(default='#000000')


    def fileLink(self):
        if self.File:
            return '<a href="' + str(self.File.url) + '">' + 'NameOfFileGoesHere' + '</a>'
        else:
            return '<a href="''"></a>'


    fileLink.allow_tags = True
    fileLink.short_description = "File Link"
