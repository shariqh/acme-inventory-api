import pytest
from src.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {'status': 'healthy'}


def test_list_inventory_returns_list(client):
    response = client.get('/api/inventory')
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_nonexistent_item_returns_404(client):
    response = client.get('/api/inventory/99999')
    assert response.status_code == 404
    assert 'error' in response.json
