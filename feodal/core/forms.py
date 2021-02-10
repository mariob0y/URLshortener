from django import forms
from shortener.models import UrlMap


class UrlCreateForm(forms.ModelForm):
    '''Form for short URL creation'''
    class Meta:
        model = UrlMap
        fields = ['full_url']
