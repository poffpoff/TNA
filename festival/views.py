from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.template import Context, loader
from festival import models


# Create your views here.



def main(request, main_r):
    main = models.Main.objects.filter(name__iexact=main_r)
    if (main):
        main = main[0]
        pages = models.Page.objects.filter(main = main)
        cards = models.Card.objects.filter(main = main)
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
    main = models.Main.objects.filter(name__iexact=main_r)
    if (main):
        main = main[0]
        pages = models.Page.objects.filter(main=main)
        page = pages.filter(name__iexact=page_r.replace("_"," ").lower())
        if (page):
            page = page[0]
            if page.to:
                if hasattr(page.to, 'thumbnailgallery'):
                    thumbnail = models.Thumbnail.objects.filter(thumbnailGallery=page.to)
                    context = {
                        'thumbnailGallery': page.to,
                        'thumbnail': thumbnail,
                    }

                    template = loader.get_template('festival/ThumbnailGallery.html')
                    return HttpResponse(template.render(context, request))
                elif hasattr(page.to, 'portfolio'):
                        folio = models.Folio.objects.filter(portFolio=page.to)
                        context = {
                            'folio': folio,
                            'portfolio': page.to,
                        }
                        template = loader.get_template('festival/portfolio.html')
                        return HttpResponse(template.render(context, request))
                elif hasattr(page.to, 'accordion'):
                        key = models.Key.objects.filter(accordion=page.to)
                        context = {
                            'key': key,
                            'accordion': page.to,
                        }
                        template = loader.get_template('festival/accordion.html')
                        return HttpResponse(template.render(context, request))
                else:
                    return HttpResponseNotFound(main_r + "/" + page_r + " does not exist")
            else:
                return HttpResponseNotFound(main_r + "/" + page_r + " does not exist")
        else:
            return HttpResponseNotFound(main_r + "/" + page_r + " does not exist")
    else:
        return HttpResponseNotFound(main_r + "/" + page_r + " does not exist")
