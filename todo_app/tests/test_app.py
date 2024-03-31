
import os
import pytest
import requests
from todo_app import app
from dotenv import load_dotenv, find_dotenv

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    load_dotenv('.env.test', override=True)

    # Create the new app.
    test_app = app.create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

    

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data
    
    def raise_for_status(self):
        pass

# Stub replacement for requests.get(url)
def stub_get(url, params={}):
    test_board_id = os.environ.get('BOARD_ID')
    api_key =  os.environ.get('TRELLO_API_KEY')
    api_token = os.environ.get('TRELLO_API_TOKEN')
    list_id_to_do = os.getenv('TO_DO_LIST_ID')
    fake_response_data = None
    if url == f'https://api.trello.com/1/boards/BOARD_ID/cards?key={api_key}&token={api_token}':
        fake_response_data = [{'idShort': 1, 'id': 123, 'name':"test",'desc': "test",'idList': list_id_to_do}]
        return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}"')

def test_index_page(monkeypatch, client):
    # Replace requests.get(url) with our own function
    monkeypatch.setattr(requests, 'get', stub_get)

    # Make a request to our app's index page
    response = client.get('/')
    assert response.status_code == 200
    assert 'test' in response.data.decode()