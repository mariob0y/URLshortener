from django.shortcuts import redirect
from django.http import HttpResponse
from shortener import shortener
from core.models import Visit
from shortener.models import UrlMap


def test(request, link):
    '''Creating short link via URL line (test purposes only)'''

    if request.user.is_authenticated:
        data = shortener.create(request.user, link)
        return HttpResponse(data)
    else:
        return HttpResponse('unauthorized')


def expand(request, link):
    '''Short URL visit data storing'''
    ip = request.META.get('HTTP_X_FORWARDED_FOR') or \
        request.META.get('REMOTE_ADDR')
    referer = request.META.get('HTTP_REFERER')
    short = UrlMap.objects.get(short_url=link)

    Visit.objects.create(ip=ip, short=short, referer=referer)

    try:
        link = shortener.expand(link)
        return redirect(link)
    except Exception as e:
        return HttpResponse(e.args)
