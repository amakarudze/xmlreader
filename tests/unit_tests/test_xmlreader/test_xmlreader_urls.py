from django.urls import reverse


def test_homepage_view(client):
    response = client.get(reverse("xmlreader:index"))
    assert response.status_code == 200
