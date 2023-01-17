import pytest


@pytest.mark.django_db
class TestSubscribeViewSet:
    endpoint = '/api/v1/subscribe/'

    def test_create(self, create_city):
        client = create_city

        payload = {'city': 'Kyiv', 'parameter': "1"}
        response = client.post(self.endpoint, payload)
        assert response.status_code == 201

    def test_list(self, create_subscribe):
        client = create_subscribe

        response = client.get(self.endpoint)
        assert response.status_code == 200

    def test_retrieve(self, create_subscribe):
        client = create_subscribe

        response = client.get(self.endpoint + '1/')
        assert response.status_code == 200

    def test_put_for_owner(self, create_subscribe):
        client = create_subscribe

        response = client.put(self.endpoint + '1/', {'city': 'Kyiv', 'parameter': "3"})
        assert response.status_code == 200

    def test_put_for_not_owner(self, create_subscribe, jwt_authenticate_second):
        client1 = create_subscribe

        client2 = jwt_authenticate_second
        response = client2.put(self.endpoint + '1/', {'city': 'Kyiv', 'parameter': '3'})
        print(response)
        assert response.status_code == 403

    def test_delete(self, create_subscribe):
        client = create_subscribe

        response = client.delete(self.endpoint + '1/')
        assert response.status_code == 204

    def test_delete_for_not_owner(self, create_subscribe, jwt_authenticate_second):
        client1 = create_subscribe

        client2 = jwt_authenticate_second
        response = client2.delete(self.endpoint + '1/')

        assert response.status_code == 403


