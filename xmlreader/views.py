from django.shortcuts import render


def index(request):
    title = "Home"
    return render(request, "xmlreader/index.html", {"title": title})


def about(request):
    title = "About"
    return render(request, "xmlreader/about.html", {"title": title})
