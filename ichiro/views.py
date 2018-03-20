from django.shortcuts import render


def index(request):
    return render("ichiro/index.html", {})
