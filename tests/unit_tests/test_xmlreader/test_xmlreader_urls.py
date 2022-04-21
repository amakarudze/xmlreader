from django.urls import reverse


def test_homepage_url(client):
    response = client.get(reverse("xmlreader:index"))
    assert response.status_code == 200


def test_about_url(client):
    response = client.get(reverse("xmlreader:about"))
    assert response.status_code == 200


def test_results_url(client, file):
    response = client.get(reverse("xmlreader:results", args=(file.pk,)))
    assert response.status_code == 200
