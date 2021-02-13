from django.shortcuts import render
from shortener import shortener
from core.forms import UrlCreateForm
from core.models import UrlMap, Visit
from django.views.generic.edit import FormView, View


class UrlCreate(FormView):
    '''Page to create short URL'''
    form_class = UrlCreateForm
    template_name = "create.html"
    success_url = '/list'

    def get_user(self, **kwargs):
        '''Getting current user'''
        user = self.request.user
        return user

    def form_valid(self, form):
        '''Validating form and creating short URL object'''
        shortener.create(self.get_user(), form.cleaned_data['full_url'])
        return super().form_valid(form)


class List(View):
    '''List all URLS created by current user'''
    def get(self, request):
        '''Getting UrlMap objects for page'''
        user = self.request.user
        queryset = UrlMap.objects.filter(user=user)
        context = {"object_list": queryset}
        return render(request, 'list.html', context)


class Stats(View):
    '''Stats of each shortened URL'''
    def get(self, request, **kwargs):
        '''Getting visit objects for page'''
        short_url = self.kwargs.get("short_url")
        url = UrlMap.objects.get(short_url=short_url)
        queryset = Visit.objects.all().filter(short=url)
        context = {"object_list": queryset}
        return render(request, 'stats.html', context)
