from main import app
import pytest

@pytest.fixture(scope='module')
def client():
    return app.test_client()