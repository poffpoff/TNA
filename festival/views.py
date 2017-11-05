from django.http import HttpResponse, Http404
from django.template import Context, loader
from festival import models
# Create your views here.



def index(request, path):
    main = models.Main.objects.filter(name=path)
    if (main):
        main = main[0]
        pages = main.pages
        cards = main.cards
        videoLink = main.video_link

        context = {
            'main' : main,
            'pages': pages,
            'cards': cards,
            'videoLink': videoLink,
        }

        template = loader.get_template('festival/event.html')
        return HttpResponse(template.render(context, request))
    else:
        return Http404(path + " does not exist")