import pytest
from application import create_app


class TestApplication():

    @pytest.fixture  # define que o valor vai ser reaproveitado
    def client(self):
        app = create_app('config.MockConfig')
        return app.test_client()

    @pytest.fixture
    def valid_user(self):
        return {
                "first_name": "Eduardo",
                "last_name": "silva",
                "cpf": "165.706.790-40",
                "email": "eduardojesus128z@gmail.com",
                "birth_date": "2001-12-13"
        }

    @pytest.fixture
    def invalid_user(self):
        return {
                "first_name": "Eduardo",
                "last_name": "silva",
                "cpf": "165.716.790-80",
                "email": "eduardojesus128z@gmail.com",
                "birth_date": "2001-12-13"
        }

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    def test_post_user(self, client, valid_user, invalid_user):
        response = client.post("/user", json=valid_user)
        assert response.status_code == 200
        assert b"included" in response.data

        response = client.post("/user", json=invalid_user)
        assert response.status_code == 400
        assert b"invalid" in response.data

        response = client.post("/user", json=valid_user)
        assert response.status_code == 404
        assert b"exists" in response.data

    def test_get_user(self, client, valid_user, invalid_user):
        response = client.get('/user/%s' % valid_user["cpf"])
        assert response.status_code == 200
        assert response.json[0]["first_name"] == "Eduardo"
        assert response.json[0]["last_name"] == "silva"
        assert response.json[0]["cpf"] == "165.706.790-40"

        birth_date = response.json[0]["birth_date"]["$date"]
        assert birth_date == "2001-12-13T00:00:00Z"

        response = client.get('/user/%s' % invalid_user["cpf"])
        assert response.status_code == 400
        assert b"exists" in response.data
