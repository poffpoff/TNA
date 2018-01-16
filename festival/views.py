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
                title = page.to.name
                text = page.to.text
                if (page.to.use_same_setting_as_main):
                    font_style = main.font_style
                    font_size = main.font_size
                    color_1 = main.color_1
                    color_2 = main.color_2
                    color_text = main.color_text
                    color_highlight = main.color_highlight
                else:
                    font_style = page.to.font_style
                    font_size = page.to.font_size
                    color_1 = page.to.color_1
                    color_2 = page.to.color_2
                    color_text = page.to.color_text
                    color_highlight = page.to.color_highlight
                if hasattr(page.to, 'thumbnailgallery'):
                    thumbnail = models.Thumbnail.objects.filter(thumbnailGallery=page.to)
                    context = {
                        'title': title,
                        'text': text,
                        'font_style' : font_style,
                        'font_size' : font_size,
                        'color_1' : color_1,
                        'color_2' : color_2,
                        'color_text' : color_text,
                        'color_highlight' : color_highlight,
                        'thumbnailGallery': page.to,
                        'thumbnail': thumbnail,
                    }

                    template = loader.get_template('festival/ThumbnailGallery.html')
                    return HttpResponse(template.render(context, request))
                elif hasattr(page.to, 'portfolio'):
                        folio = models.Folio.objects.filter(portFolio=page.to)
                        context = {
                            'title': title,
                            'text': text,
                            'font_style' : font_style,
                            'font_size' : font_size,
                            'color_1' : color_1,
                            'color_2' : color_2,
                            'color_highlight' : color_highlight,
                            'color_text' : color_text,
                            'folio': folio,
                            'portfolio': page.to,
                        }
                        template = loader.get_template('festival/portfolio.html')
                        return HttpResponse(template.render(context, request))
                elif hasattr(page.to, 'accordion'):
                        key = models.Key.objects.filter(accordion=page.to)
                        context = {
                            'title': title,
                            'text': text,
                            'font_style' : font_style,
                            'font_size' : font_size,
                            'color_1' : color_1,
                            'color_2' : color_2,
                            'color_text' : color_text,
                            'color_highlight' : color_highlight,
                            'key': key,
                            'accordion': page.to,
                        }
                        template = loader.get_template('festival/accordion.html')
                        return HttpResponse(template.render(context, request))
                elif hasattr(page.to, 'googlemap'):
                        map = models.GoogleMap.objects.filter(name=page.to.name)[0]
                        context = {
                            'title': title,
                            'text': text,
                            'font_style' : font_style,
                            'font_size' : font_size,
                            'color_1' : color_1,
                            'color_2' : color_2,
                            'color_text' : color_text,
                            'color_highlight' : color_highlight,
                            'map': map,
                            'map.src': map.src,
                        }
                        template = loader.get_template('festival/googleMap.html')
                        return HttpResponse(template.render(context, request))
                else:
                    return HttpResponseNotFound(main_r + "/" + page_r + " does not exist")
            else:
                return HttpResponseNotFound(main_r + "/" + page_r + " does not exist")
        else:
            return HttpResponseNotFound(main_r + "/" + page_r + " does not exist")
    else:
        return HttpResponseNotFound(main_r + "/" + page_r + " does not exist")
