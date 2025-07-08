import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app 

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_buscar_existente(client):
    response = client.post("/buscar", data={"documentoIdentidad":  "12345678A"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Laura" in response.data

def test_buscar_inexistente(client):
    response = client.post("/buscar", data={"documentoIdentidad": "00000000X"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Ciudadano/a no encontrado" in response.data 