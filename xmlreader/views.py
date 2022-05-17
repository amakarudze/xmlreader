import io, xmltodict

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse

from .forms import UploadFileForm
from .models import Upload


def index(request):
    title = "Home"
    files = Upload.objects.all()
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            return redirect(reverse("xmlreader:results", args=(file.pk,)))
    else:
        form = UploadFileForm()
    return render(
        request, "xmlreader/index.html", {"title": title, "form": form, "files": files}
    )


def about(request):
    title = "About"
    return render(request, "xmlreader/about.html", {"title": title})


def results(request, id):
    title = "Decoded File"
    file = get_object_or_404(Upload, id=id)

    with file.file.open(mode="rb") as xml_file:
        data_dict = xmltodict.parse(xml_file.read())

    return render(
        request, "xmlreader/results.html", {"title": title, "data_dict": data_dict}
    )
