from django.http import HttpResponse
from django.template import Context, loader
from festival import models
# Create your views here.



def tna(request):
    main = models.Main.objects.get(name="Track'n'Art")
    main = main
    pages = main.pages
    cards = main.cards
    videoLink = main.video_link

    context = {
        'main' : main,
        'pages': pages,
        'cards': cards,
        'videoLink': videoLink,
    }

    template = loader.get_template('festival/tna.html')
    return HttpResponse(template.render(context, request))
