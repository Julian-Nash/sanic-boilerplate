import pytest
from sanic_testing import TestManager

from app import create_app
from app.config import ConfigEnum


@pytest.fixture
def app():
    sanic_app = create_app(ConfigEnum.TEST.value)
    TestManager(sanic_app)
    return sanic_app


@pytest.mark.asyncio
async def test_basic_asgi_client(app):
    request, response = await app.asgi_client.get("/")
    assert response.status == 200
