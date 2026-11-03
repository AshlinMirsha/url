import pytest
import app as app_module

# Create test client
@pytest.fixture
def client():

    app_module.app.config['TESTING'] = True

    app_module.URL_database.clear()

    with app_module.app.test_client() as client:
        yield client

    app_module.URL_database.clear()


# Test 1: Check homepage
def test_homepage(client):

    response = client.get('/')

    assert response.status_code == 200


# Test 2: Test URL submission
def test_shorten_url(client, monkeypatch):

    monkeypatch.setattr(
        app_module,
        'generate_short_url',
        lambda: 'Ab12Cd'
    )

    response = client.post(
        '/',
        data={'URL': 'https://www.google.com'}
    )

    assert response.status_code == 200

    assert b'Ab12Cd' in response.data

    assert app_module.URL_database['Ab12Cd'] == 'https://www.google.com'


# Test 3: Test URL redirection
def test_redirect_url(client):

    app_module.URL_database['Ab12Cd'] = 'https://www.google.com'

    response = client.get('/Ab12Cd')

    assert response.status_code == 302

    assert response.location == 'https://www.google.com'


# Test 4: Test invalid URL
def test_invalid_url(client):

    response = client.get('/wrongcode')

    assert response.status_code == 404


# Test 5: Check CSS file
def test_css_file(client):

    response = client.get('/static/style.css')

    assert response.status_code == 200


# Test 6: Check JavaScript file
def test_js_file(client):

    response = client.get('/static/script.js')

    assert response.status_code == 200
