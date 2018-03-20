import ichiro.views
from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url
admin.autodiscover()


urlpatterns = [
    url(r'^$', ichiro.views.index, name='index'),
    path('admin/', admin.site.urls),
]
