from django.http import HttpResponse
from ichiro.models import Scrape


def index(request):
    """
    The data.
    """
    obj = Scrape.objects.latest()
    return HttpResponse(obj.json, content_type="application/javascript")
