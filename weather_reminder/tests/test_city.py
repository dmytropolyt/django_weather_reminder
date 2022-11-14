import pytest


@pytest.mark.django_db
class TestCityViewSet:
    endpoint = '/api/v1/city/'

    def test_create_city(self, jwt_authenticate):
        client = jwt_authenticate
        payload = {'name': 'Kyiv'}

        response = client.post(self.endpoint, payload)
        assert response.status_code == 201
        assert response.data['name'] == payload['name']

    def test_list(self, create_city):
        client = create_city

        response = client.get(self.endpoint)
        assert response.status_code == 200

    def test_retrieve(self, create_city):
        client = create_city

        response = client.get(self.endpoint + '1/')
        assert response.status_code == 200

    def test_put_for_not_admin_user(self, create_city):
        client = create_city

        response = client.put(self.endpoint + '1/', {'name': 'Berlin'})
        assert response.status_code == 403

    def test_put_for_admin_user(self, jwt_authenticate_for_admin):
        client = jwt_authenticate_for_admin
        payload = {'name': 'Kyiv'}
        client.post(self.endpoint, payload)

        response = client.put(self.endpoint + '1/', {'name': 'Berlin'})
        assert response.status_code == 200

    def test_delete_for_not_admin_user(self, create_city):
        client = create_city

        response = client.delete(self.endpoint + '1/')
        assert response.status_code == 403

    def test_delete_for_admin_user(self, jwt_authenticate_for_admin):
        client = jwt_authenticate_for_admin
        payload = {'name': 'Kyiv'}
        client.post(self.endpoint, payload)

        response = client.delete(self.endpoint + '1/')
        assert response.status_code == 204
