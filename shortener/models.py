from django.db import models
from django.conf import settings


class UrlMap(models.Model):
    '''Storing of full and short URL'''
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    full_url = models.CharField(max_length=500)
    short_url = models.CharField(max_length=50, unique=True, db_index=True)
    usage_count = models.IntegerField(default=0)
    max_count = models.IntegerField(default=-1)
    lifespan = models.IntegerField(default=-1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_expired = models.DateTimeField()

    def __str__(self):
        return '{} - {} - {}'.format(self.user, self.full_url, self.short_url)


class UrlProfile(models.Model):
    '''Settings for URS shortening usage'''
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True, null=True)
    max_urls = models.IntegerField(default=-1, null=True, blank=True)
    max_concurrent_urls = models.IntegerField(default=100, null=True,
                                              blank=True)
    default_lifespan = models.IntegerField(default=120, null=True,
                                           blank=True)
    default_max_uses = models.IntegerField(default=-1, null=True,
                                           blank=True)

    def __str__(self):
        return '{}'.format(self.user)
