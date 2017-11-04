from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from festival import models
# Create your views here.

def twitterBootStrapExample(request):
    template = loader.get_template('festival/twitterBootStrapExample.html')
    return HttpResponse(template.render())

def verticalCollapse(request):
    template = loader.get_template('festival/verticalCollapse.html')
    return HttpResponse(template.render())

def sideBar(request):
    template = loader.get_template('festival/sideBar.html')
    return HttpResponse(template.render())

def carrousel(request):
    main = models.Main.objects.get(name="Track'n'Art")
    pages = main.pages
    links = main.links
    videoLink = main.video_link

    context = {
        'pages': pages,
        'links': links,
        'videoLink': videoLink,
    }

    template = loader.get_template('festival/carrousel.html')
    return HttpResponse(template.render(context, request))

def carrousel1(request):
    main = models.Main.objects.get(name="Track'n'Art")
    pages = main.pages
    links = main.links
    videoLink = main.video_link

    context = {
        'pages': pages,
        'links': links,
        'videoLink': videoLink,
    }

    template = loader.get_template('festival/carrousel1.html')
    return HttpResponse(template.render(context, request))

def tna(request):
    main = models.Main.objects.get(name="Track'n'Art")
    main = main
    pages = main.pages
    links = main.links
    videoLink = main.video_link

    context = {
        'main' : main,
        'pages': pages,
        'links': links,
        'videoLink': videoLink,
    }

    template = loader.get_template('festival/tna.html')
    return HttpResponse(template.render(context, request))

def grayscale(request):
    template = loader.get_template('festival/grayscale.html')
    return HttpResponse(template.render())

def landing(request):
    template = loader.get_template('festival/landing.html')
    return HttpResponse(template.render())