import requests
from configuration import TESTS_URL

def test_getting_posts():
    response = requests.get(TESTS_URL)
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) > 0