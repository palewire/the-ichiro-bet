from django.conf import settings
from django.http import HttpResponse


def index(request):
    """
    The data.
    """
    file = open(settings.ICHIRO_JSON, 'rb')
    data = file.read()
    file.close()
    return HttpResponse(data, content_type="application/javascript")
