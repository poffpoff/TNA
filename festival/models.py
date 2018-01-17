from django.db import models
from colorfield.fields import ColorField


# Create your models here.

class PageType(models.Model):
    name = models.CharField(max_length=99)
    text = models.TextField(max_length=999,blank=True)
    font_size = models.IntegerField(default='16')

    transparent_text_background = models.BooleanField(default=False)

    use_image_as_text_background = models.BooleanField(default=False)
    no_repeat_text_image = models.BooleanField(default=False)
    background_text_image = models.FileField('File', upload_to='./festival/userImages/', blank=True)

    use_same_setting_as_main = models.BooleanField(default=True)

    color_1 = ColorField(default='#000000')
    color_2 = ColorField(default='#FFFFFF')
    color_highlight = ColorField(default='#FFFFFF')

    font_style = models.CharField(max_length=99, default='Crimson Text')

    use_image_as_background = models.BooleanField(default=False)
    no_repeat_image = models.BooleanField(default=True)
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
    accordion = models.ForeignKey(Accordion, blank=True)
    name = models.CharField(max_length=99, default="", blank=True)
    text = models.TextField(max_length=999, default='', blank=True)

    def __str__(self):
        return str(self.name)

class ThumbnailGallery(PageType):

    def __str__(self):
        return str(self.name)


class Thumbnail(models.Model):
    thumbnailGallery = models.ForeignKey(ThumbnailGallery, blank=True)
    name = models.CharField(max_length=99, default="")
    image = models.FileField('File', upload_to='./festival/userImages/')
    link = models.URLField(blank=True)


    def __str__(self):
        return str(self.name)

class Portfolio(PageType):

    def __str__(self):
        return str(self.name)


# class Folio du portefolio
class Folio(models.Model):
    portFolio = models.ForeignKey(Portfolio, blank=True)
    name = models.CharField(max_length=99, default="")
    image = models.FileField('File', upload_to='./festival/userImages/')
    text = models.TextField(max_length=999, default='')
    link = models.URLField(blank=True)


    def __str__(self):
        return str(self.name)


class Main(models.Model):
    name = models.CharField(max_length=99)

    color_1 = ColorField(default='#000000')
    color_2 = ColorField(default='#FFFFFF')
    color_highlight = ColorField(default='#FFFFFF')

    font_style = models.CharField(max_length=50, default='Crimson Text')
    font_size = models.IntegerField(default='22')

    use_side_bar_image = models.BooleanField(default=False)
    side_bar_image = models.FileField('File', upload_to='./festival/userImages/', blank=True)

    video_link = models.URLField(blank=True)

    use_image_as_background = models.BooleanField(default=False)
    no_repeat_image = models.BooleanField(default=True)
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
    name = models.CharField(max_length=99)
    to = models.ForeignKey(PageType, null=True, blank=True)
    main = models.ForeignKey(Main, on_delete=models.CASCADE)

    def normalizedName(self):
        return str(self.name).replace(" ","_").lower()

    def __str__(self):
        return str(self.name)


class Card(models.Model):
    name = models.CharField(max_length=99)
    image = models.FileField('File', upload_to='./festival/userImages/')
    https = models.CharField(max_length=999, default="#")
    main = models.ForeignKey(Main, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    def fileLink(self):
        if self.File:
            return '<a href="' + str(self.File.url) + '">' + 'NameOfFileGoesHere' + '</a>'
        else:
            return '<a href="''"></a>'

    fileLink.allow_tags = True
    fileLink.short_description = "File Link"


class FirstPage(models.Model):
    title = models.CharField(max_length=99)
    font_style = models.CharField(max_length=50, default='Crimson Text')
    font_size = models.IntegerField(default='22')
    color_1 = ColorField(default='#000000')
    color_2 = ColorField(default='#FFFFFF')
    use_image_as_background = models.BooleanField(default=False)
    no_repeat_image = models.BooleanField(default=True)
    background_image = models.FileField('File', upload_to='./festival/userImages/', blank=True)

class Index(models.Model):
    name = models.CharField(max_length=99)
    to = models.ForeignKey(Main, null=True, blank=True)
    image = models.FileField('File', upload_to='./festival/userImages/')
    firstPage = models.ForeignKey(FirstPage, blank=True, on_delete=models.CASCADE)
