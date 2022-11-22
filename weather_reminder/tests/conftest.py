import pytest
from rest_framework.test import APIClient


@pytest.fixture
def test_password():
    return 'strong-test-pass'


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'username' not in kwargs:
            kwargs['username'] = 'dmytropolyt'
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def jwt_authenticate(db, create_user, client, test_password):
    user = create_user()
    jwt = client.post('/api/token/', {'username': user.username, 'password': test_password})
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt.data['access'])
    return client


@pytest.fixture
def jwt_authenticate_for_admin(db, create_user, client, test_password):
    user = create_user(is_staff=True)
    jwt = client.post('/api/token/', {'username': user.username, 'password': test_password})
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt.data['access'])
    return client


@pytest.fixture
def create_city(db, jwt_authenticate):
    client = jwt_authenticate
    payload = {'name': 'Kyiv'}
    client.post('/api/v1/city/', payload)
    return client

@pytest.fixture
def create_subscribe(db, create_city):
    client = create_city
    payload = {'city': 'Kyiv', 'parameter': 2}
    client.post('/api/v1/subscribe/', payload)
    return client

