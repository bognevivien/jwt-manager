import pytest
from jwt_manager.api.jwt_service import JWTService

def test_get_jwt():
    auth_service = JWTService()
    jwt_result = auth_service.get_jwt()
    assert jwt_result is not None
