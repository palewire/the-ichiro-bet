import json
from django.http import HttpResponse
from ichiro.models import Scrape, Projection


def latest_scrape(request):
    """
    A dump of all the latest scraped data.
    """
    obj = Scrape.objects.latest()
    return HttpResponse(obj.json, content_type="application/javascript")


def projections_by_date(request):
    """
    A history of all the projection data by date.
    """
    obj = Projection.objects.by_date()
    return HttpResponse(json.dumps(obj), content_type="application/javascript")
