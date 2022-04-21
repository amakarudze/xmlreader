import os
import pytest

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

from xmlreader.models import Upload


@pytest.fixture
def file(db):
    return Upload.objects.create(
        file="google.com!djangogirls.org!1649808000!1649894399 2.xml"
    )


@pytest.fixture
def file_data():
    fpath = os.path.join(
        settings.BASE_DIR, "xml_files/google.comdjangogirls.org16498080001649894399.xml"
    )
    filename = "google.comdjangogirls.org16498080001649894399.xml"
    file = open(fpath, "rb")
    file_dict = {"file": SimpleUploadedFile(filename, bytes(file))}
    return file_dict


@pytest.fixture
def upload_form_valid(file):
    data = {"file": "google.comdjangogirls.org16498080001649894399.xml"}
    return data


@pytest.fixture
def upload_form_invalid():
    data = {"file": ""}
    return data
