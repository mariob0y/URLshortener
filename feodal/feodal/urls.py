from django.contrib import admin
from django.urls import path, include
from core.views import UrlCreate, List, Stats
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('s/', include('shortener.urls')),
    path('create/', login_required(UrlCreate.as_view())),
    path('list/', login_required(List.as_view())),
    path('s/<str:short_url>/stats', login_required(Stats.as_view())),
]
