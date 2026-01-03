import requests
from configuration import TESTS_URL
from tests.src.enums.global_enums import GlobalErrorssages
from jsonschema import validate
from src.shemas.post import POST_SCHEMA

def test_getting_posts():
    response = requests.get(TESTS_URL)
    assert response.status_code == 200, GlobalErrorssages.WRONG_STATUS_CODE.value
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) > 0
    
    validate(recived_posts, POST_SCHEMA)