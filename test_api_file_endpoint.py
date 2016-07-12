import requests
import pytest
xfail = pytest.mark.xfail


def test_artists_endpoint_shows_entire_list():
    response = requests.get("http://127.0.0.1:8000/files/")
    assert len(response.json()['data']) == 1


