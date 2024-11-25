import pytest
from jwt_manager.cache import RedisCache

def test_redis_cache():
    cache = RedisCache()
    cache.set("test_key", "test_value")
    value = cache.get("test_key")
    assert value == "test_value"
    cache.delete("test_key")
    value = cache.get("test_key")
    assert value is None
