from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.template import Context, loader
from festival import models


# Create your views here.



def main(request, main_r):
    main = models.Main.objects.filter(name=main_r)
    if (main):
        main = main[0]
        pages = main.pages
        cards = main.cards
        videoLink = main.video_link

        context = {
            'main': main,
            'pages': pages,
            'cards': cards,
            'videoLink': videoLink,
        }

        template = loader.get_template('festival/event.html')
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseNotFound(main_r + " does not exist")


def page(request, main_r, page_r):
    main = models.Main.objects.filter(name=main_r)
    if (main):
        page = models.Page.objects.filter(name=page_r)
        if (page):
            page = page[0]
            if (page.to):
                if (type(page.to) is models.Calendar):
                    calendar = page.to
                    events = calendar.events
                    dates = calendar.get_dates
                    context = {
                        'calendar': calendar,
                        'events': events,
                        'dates': dates,
                    }

                    template = loader.get_template('festival/calendar.html')
                    return HttpResponse(template.render(context, request))
                else:
                    return HttpResponseNotFound(main_r + "/" + page_r + " does not exist")
            else:
                return HttpResponseNotFound(main_r + "/" + page_r + " does not exist")
        else:
            return HttpResponseNotFound(main_r + "/" + page_r + " does not exist")
    else:
        return HttpResponseNotFound(main_r + "/" + page_r + " does not exist")
