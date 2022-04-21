import os

from django.conf import settings
from django.urls import reverse


def test_index_view(client):
    with open(
        os.path.join(
            settings.BASE_DIR,
            "xml_files/google.com!djangogirls.org!1649808000!1649894399.xml",
        ),
        "rb",
    ) as fp:
        response = client.post(
            reverse("xmlreader:index"), {"name": "test_file", "attachment": fp}
        )
    assert response.status_code == 200


def test_results_view(client, file):
    response = client.get(reverse("xmlreader:results", args=(file.pk,)))
    assert response.status_code == 200
