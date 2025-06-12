from http.client import responses

from django.test import TestCase

# Create your tests here.
import pytest
from django.contrib.auth.hashers import make_password
from rest_framework.test import APIClient
from user.models import User


class TestAuth:
    @pytest.fixture # clone database
    def api_client(self):
        User.objects.create(first_name="Botir" , email="absaitovdev@gmail.com" , username="botir" , password=make_password("1") , phone="993583234" , role="admin")
        User.objects.create(first_name="kamol" , email="kamol@gmail.com" , username="kamol" , password=make_password("2") , phone="993583232")
        return APIClient()

    @pytest.mark.django_db
    def test_login(self, api_client):
        response = api_client.post("http://localhost:8000/login", {
            "username": "botir",
            "password": "1"
        }, format="json")
        assert 300>response.status_code >= 200 , "Bad Request"
        assert "access" in response.json().keys()
        assert "refresh" in response.json().keys()

    @pytest.mark.django_db
    def test_register(self, api_client):
        response = api_client.post("http://localhost:8000/api/v1/auth/register", {
              "username": "john",
              "email": "bsarvar265@example.com",
              "password": "1",
              "phone": "991231212",
              "first_name": "sarvar"
            }, format="json")
        assert response.json().get("password").startswith("pbkdf2") == True
        assert response.status_code == 201
        assert User.objects.filter(email="bsarvar265@example.com").exists() == True

    @pytest.mark.django_db
    def test_verify_otp(self, api_client):
        response = api_client.post("http://localhost:8000/api/v1/auth/verify-otp", {
            "email" : "bsarvar265@example.com",
            "code" : "123456"
        })
        assert response.status_code == 200
        assert response.json().get("status") == "True"




    # @pytest.mark.django_db
    # def test_profile_about(self, api_client):
    #     response = api_client.post("http://localhost:8000/login", {
    #         "username": "botir",
    #         "password": "1"
    #     }, format="json")
    #
    #     data = response.json()
    #     access_token = data.get("access")
    #     headers = {
    #         "Authorization": f"Bearer {access_token}"
    #     }
    #     response = api_client.get("http://localhost:8000/api/v1/auth/profile/about" ,headers=headers )
    #     data = response.json()
    #     assert response.status_code == 200
    #     assert data.get("user").get("phone") == "993583234"

    # @pytest.mark.django_db
    # def test_profile_delete(self, api_client):
    #     response = api_client.post("http://localhost:8000/api/v1/auth/login", {
    #         "username": "botir",
    #         "password": "1"
    #     }, format="json")
    #
    #     data = response.json()
    #     access_token = data.get("access")
    #     headers = {
    #         "Authorization": f"Bearer {access_token}"
    #     }
    #     response = api_client.delete("http://localhost:8000/api/v1/auth/profile/2", format="json" , headers=headers)
    #     assert response.status_code == 204
    #     assert User.objects.filter(email="kamol@gmail.com").exists() == False
    #






