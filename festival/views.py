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
        font_style = main.font_style
        font_size = main.font_size
        color_1 = main.color_1
        color_2 = main.color_2
        color_highlight = main.color_highlight
        context = {
            'main': main,
            'pages': pages,
            'cards': cards,
            'videoLink': videoLink,
            'font_style': font_style,
            'font_size': font_size,
            'color_1': color_1,
            'color_2': color_2,
            'color_highlight': color_highlight,
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
            page = page.to
            if page:
                title = page.name
                text = page.text
                pages = models.Page.objects.filter(main = main)
                if (page.use_same_setting_as_main):
                    font_style = main.font_style
                    font_size = main.font_size
                    color_1 = main.color_1
                    color_2 = main.color_2
                    color_highlight = main.color_highlight
                else:
                    font_style = page.font_style
                    font_size = page.font_size
                    color_1 = page.color_1
                    color_2 = page.color_2
                    color_highlight = page.color_highlight
                if hasattr(page, 'thumbnailgallery'):
                    thumbnail = models.Thumbnail.objects.filter(thumbnailGallery=page)
                    context = {
                        'main': main,
                        'page': page,
                        'pages': pages,
                        'title': title,
                        'text': text,
                        'font_style' : font_style,
                        'font_size' : font_size,
                        'color_1' : color_1,
                        'color_2' : color_2,
                        'color_highlight' : color_highlight,
                        'thumbnailGallery': page,
                        'thumbnail': thumbnail,
                    }

                    template = loader.get_template('festival/ThumbnailGallery.html')
                    return HttpResponse(template.render(context, request))
                elif hasattr(page, 'portfolio'):
                        folio = models.Folio.objects.filter(portFolio=page)
                        context = {
                            'main': main,
                            'page': page,
                            'pages': pages,
                            'title': title,
                            'text': text,
                            'font_style' : font_style,
                            'font_size' : font_size,
                            'color_1' : color_1,
                            'color_2' : color_2,
                            'color_highlight' : color_highlight,
                            'folio': folio,
                            'portfolio': page,
                        }
                        template = loader.get_template('festival/portfolio.html')
                        return HttpResponse(template.render(context, request))
                elif hasattr(page, 'accordion'):
                        key = models.Key.objects.filter(accordion=page)
                        context = {
                            'main': main,
                            'page': page,
                            'pages': pages,
                            'title': title,
                            'text': text,
                            'font_style' : font_style,
                            'font_size' : font_size,
                            'color_1' : color_1,
                            'color_2' : color_2,
                            'color_highlight' : color_highlight,
                            'key': key,
                            'accordion': page,
                        }
                        template = loader.get_template('festival/accordion.html')
                        return HttpResponse(template.render(context, request))
                elif hasattr(page, 'googlemap'):
                        map = models.GoogleMap.objects.filter(name=page.name)[0]
                        context = {
                            'main': main,
                            'page': page,
                            'pages': pages,
                            'title': title,
                            'text': text,
                            'font_style' : font_style,
                            'font_size' : font_size,
                            'color_1' : color_1,
                            'color_2' : color_2,
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
