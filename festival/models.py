from django.db import models
from colorfield.fields import ColorField


# Create your models here.

class Page(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
        return str(self.name)


class Card(models.Model):
    name = models.CharField(max_length=30, default="card")
    image = models.FileField('File', upload_to='./festival/userImages/')
    https = models.CharField(max_length=999, default="#")

    def __str__(self):
        return str(self.name)

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

    use_image_in_front_of_video = models.BooleanField(default=False)
    image_in_front_of_video = models.FileField('File', upload_to='./festival/userImages/')

    cards = models.ManyToManyField(Card)
    pages = models.ManyToManyField(Page)

    color_1 = ColorField(default='#000000')
    color_2 = ColorField(default='#FFFFFF')
    color_highlight = ColorField(default='#FFFFFF')

    use_image_as_background = models.BooleanField(default=False)
    no_repeat_image = models.BooleanField(default=False)
    background_image = models.FileField('File', upload_to='./festival/userImages/')


    use_side_bar_image = models.BooleanField(default=False)
    side_bar_image = models.FileField('File', upload_to='./festival/userImages/')



    font_style_navigation_bar = models.CharField( max_length =50, default='Crimson Text')
    font_size_navigation_bar = models.IntegerField(default='22')


    def __str__(self):
        return str(self.name)


    def fileLink(self):
        if self.File:
            return '<a href="' + str(self.File.url) + '">' + 'NameOfFileGoesHere' + '</a>'
        else:
            return '<a href="''"></a>'


    fileLink.allow_tags = True
    fileLink.short_description = "File Link"


