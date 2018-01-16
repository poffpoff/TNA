from django.db import models
from colorfield.fields import ColorField


# Create your models here.

class PageType(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField(max_length=999, default='')

    transparent_text_background = models.BooleanField(default=False)


    use_same_setting_as_main = models.BooleanField(default=True)

    color_1 = ColorField(default='#000000')
    color_2 = ColorField(default='#FFFFFF')
    color_text = ColorField(default='#000000')
    color_highlight = ColorField(default='#FFFFFF')

    font_style = models.CharField(max_length=50, default='Crimson Text')
    font_size = models.IntegerField(default='22')

    use_image_as_background = models.BooleanField(default=False)
    no_repeat_image = models.BooleanField(default=False)
    background_image = models.FileField('File', upload_to='./festival/userImages/', blank=True)

    def __str__(self):
        return str(self.name)

class GoogleMap(PageType):
    src = models.URLField(blank=True)
    def __str__(self):
        return str(self.name)

class Accordion(PageType):

    def __str__(self):
        return str(self.name)


class Key(models.Model):
    accordion = models.ForeignKey(Accordion, default=0)
    name = models.CharField(max_length=30, default="")
    text = models.TextField(max_length=999, default='')

    def __str__(self):
        return str(self.name)

class ThumbnailGallery(PageType):

    def __str__(self):
        return str(self.name)


class Thumbnail(models.Model):
    thumbnailGallery = models.ForeignKey(ThumbnailGallery, default=0)
    name = models.CharField(max_length=30, default="")
    image = models.FileField('File', upload_to='./festival/userImages/')
    link = models.URLField(blank=True)


    def __str__(self):
        return str(self.name)

class Portfolio(PageType):

    def __str__(self):
        return str(self.name)


# class Folio du portefolio
class Folio(models.Model):
    portFolio = models.ForeignKey(Portfolio, default=0)
    name = models.CharField(max_length=30, default="")
    image = models.FileField('File', upload_to='./festival/userImages/')
    text = models.TextField(max_length=999, default='')
    link = models.URLField(blank=True)


    def __str__(self):
        return str(self.name)


class Main(models.Model):
    name = models.CharField(max_length=30)

    color_1 = ColorField(default='#000000')
    color_2 = ColorField(default='#FFFFFF')
    color_text = ColorField(default='#000000')
    color_highlight = ColorField(default='#FFFFFF')

    font_style = models.CharField(max_length=50, default='Crimson Text')
    font_size = models.IntegerField(default='22')

    use_side_bar_image = models.BooleanField(default=False)
    side_bar_image = models.FileField('File', upload_to='./festival/userImages/', blank=True)

    video_link = models.URLField(blank=True)

    use_image_as_background = models.BooleanField(default=False)
    no_repeat_image = models.BooleanField(default=False)
    background_image = models.FileField('File', upload_to='./festival/userImages/', blank=True)

    use_image_as_side_bar_background = models.BooleanField(default=False)
    no_repeat_side_bar_image = models.BooleanField(default=False)
    background_side_bar_image = models.FileField('File', upload_to='./festival/userImages/', blank=True)

    show_instagram = models.BooleanField(default=False)
    https_instagram = models.CharField(max_length=999, default="#")

    show_facebook = models.BooleanField(default=False)
    https_facebook = models.CharField(max_length=999, default="#")

    show_twitter = models.BooleanField(default=False)
    https_twitter = models.CharField(max_length=999, default="#")

    show_snapchat = models.BooleanField(default=False)
    https_snapchat = models.CharField(max_length=999, default="#")

    show_youtube = models.BooleanField(default=False)
    https_youtube = models.CharField(max_length=999, default="#")

    show_contact_us = models.BooleanField(default=False)
    https_contact_us = models.CharField(max_length=999, default="#")

    use_official_color_for_icons = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    def fileLink(self):
        if self.File:
            return '<a href="' + str(self.File.url) + '">' + 'NameOfFileGoesHere' + '</a>'
        else:
            return '<a href="''"></a>'

    fileLink.allow_tags = True
    fileLink.short_description = "File Link"


class Page(models.Model):
    name = models.CharField(max_length=30)
    to = models.ForeignKey(PageType, null=True, blank=True)
    main = models.ForeignKey(Main, on_delete=models.CASCADE)

    def normalizedName(self):
        return str(self.name).replace(" ","_").lower()

    def __str__(self):
        return str(self.name)


class Card(models.Model):
    name = models.CharField(max_length=30)
    image = models.FileField('File', upload_to='./festival/userImages/')
    https = models.CharField(max_length=999, default="#")
    main = models.ForeignKey(Main, default=0, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    def fileLink(self):
        if self.File:
            return '<a href="' + str(self.File.url) + '">' + 'NameOfFileGoesHere' + '</a>'
        else:
            return '<a href="''"></a>'

    fileLink.allow_tags = True
    fileLink.short_description = "File Link"
