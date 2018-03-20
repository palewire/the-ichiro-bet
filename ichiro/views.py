from django.http import HttpResponse


def index(request):
    """
    The data.
    """
    file = open("ichiro.json", 'rb')
    data = file.read()
    file.close()
    return HttpResponse(data, content_type="application/javascript")
