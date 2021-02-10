from django.db import models
from shortener.models import UrlMap


class Visit(models.Model):
    '''Data of short URL visit'''
    short = models.ForeignKey(UrlMap, on_delete=models.CASCADE)
    ip = models.TextField()
    referer = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.short} - {self.ip}  - {self.date}'
