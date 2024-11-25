import pytest
from jwt_manager.auth import AuthService

def test_get_access_token():
    auth_service = AuthService()
    access_token = auth_service.get_access_token()
    assert access_token is not None

def test_get_jwt_token():
    auth_service = AuthService()
    access_token = auth_service.get_access_token()
    jwt_token = auth_service.get_jwt_token(access_token)
    assert jwt_token is not None
