import pytest
from rest_framework.test import APIClient

#client = APIClient()


@pytest.mark.django_db
def test_register_user(client):
    payload = {
        'username': 'dmytropolyt',
        'email': 'dima@ukr.net',
        'password': '121212qd',
        'first_name': 'Dmytro',
        'last_name': 'Konstantinov'
    }

    response = client.post("/api/v1/register", payload)
    data = response.data

    assert payload['username'] == data['user']['username']
    assert payload['email'] == data['user']['email']


@pytest.mark.django_db
def test_login_user(client, create_user, test_password):
    user = create_user()
    response = client.post('/api-auth/login/', {'username': user.username, 'password': test_password})

    assert response.status_code == 302
