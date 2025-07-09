import sys
import os
import pytest 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

DATOS_CIUDADANO_BASE = {
    "nombre": "Luis",
        "apellido1": "Ramírez", 
        "apellido2": "Cano",
        "dni": "12345678A",

        "telefono": "600123456",
        "correoElectronico": "luis@example.com",
        "municipio": "Llanera",
        "direccion_texto": "Calle Ejemplo, 123",
        "codPostal": "33424",

        "observaciones": "Sin observaciones"
}
@pytest.mark.validation_nombre

# Tests para datos correctos
def test_nuevo_ciudadano_valido(client):
    datos=DATOS_CIUDADANO_BASE.copy()
    response = client.post('/nuevo', data=datos, follow_redirects=True)
    assert response.status_code == 200
    assert b"Informe" in response.data
    
def test_nuevo_ciudadano_validoEspacios(client):
    datos=DATOS_CIUDADANO_BASE.copy()
    datos["nombre"] = "José Luís"
    response = client.post('/nuevo', data=datos, follow_redirects=True)
    assert response.status_code == 200
    assert b"Informe" in response.data
    
def test_nuevo_ciudadano_validoApellido1(client):
    datos = DATOS_CIUDADANO_BASE.copy()
    datos["apellido1"] = "Del Río"
    response = client.post('/nuevo', data=datos, follow_redirects=True)
    assert response.status_code == 200
    assert b"Informe" in response.data

def test_nuevo_ciudadano_validoApellido2(client):
    datos = DATOS_CIUDADANO_BASE.copy()
    datos["apellido2"] = "Del Río"
    response = client.post('/nuevo', data=datos, follow_redirects=True)
    assert response.status_code == 200
    assert b"Informe" in response.data

def test_nuevo_ciudadano_validoGuiones1(client):
    datos = DATOS_CIUDADANO_BASE.copy()
    datos["apellido1"] = "Pérez-Gómez"
    response = client.post('/nuevo', data=datos, follow_redirects=True)
    assert response.status_code == 200
    assert b"Informe" in response.data

def test_nuevo_ciudadano_validoGuiones2(client):
    datos = DATOS_CIUDADANO_BASE.copy()
    datos["apellido2"] = "Pérez-Gómez"
    response = client.post('/nuevo', data=datos, follow_redirects=True)
    assert response.status_code == 200
    assert b"Informe" in response.data

#Tests para datos incorrectos
def test_nuevo_ciudadano_nombreIncorrectoNumero(client):
    datos = DATOS_CIUDADANO_BASE.copy()
    datos["nombre"] = "Luí3"
    response = client.post('/nuevo', data= datos, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_nombreIncorrectoSigno(client):
    datos = DATOS_CIUDADANO_BASE.copy()
    datos["nombre"] = "Luí+"
    response = client.post('/nuevo', data= datos, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_apellido1IncorrectoNumero(client):
    datos = DATOS_CIUDADANO_BASE.copy()
    datos["apellido1"] = "Ramíre3"
    response = client.post('/nuevo', data= datos, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_apellido1IncorrectoSigno(client):
    datos = DATOS_CIUDADANO_BASE.copy()
    datos["apellido1"] = "Ramíre+"
    response = client.post('/nuevo', data= datos, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_apellido2IncorrectoNumero(client):
    datos = DATOS_CIUDADANO_BASE.copy()
    datos["apellido2"] = "Garci3"
    response = client.post('/nuevo', data= datos, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_apellido2IncorrectoSigno(client):
    datos = DATOS_CIUDADANO_BASE.copy()
    datos["apellido2"] = "Cano+"
    response = client.post('/nuevo', data= datos, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_teléfonoIncorrectoCorto(client):
    datos = DATOS_CIUDADANO_BASE.copy()
    datos["telefono"] = "60012345"
    response = client.post('/nuevo', data= datos, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_teléfonoIncorrectoLargo(client):
    datos = DATOS_CIUDADANO_BASE.copy()
    datos["telefono"] = "6001234567"
    response = client.post('/nuevo', data= datos, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_teléfonoIncorrectoLetra(client):
    datos = DATOS_CIUDADANO_BASE.copy()
    datos["telefono"] = "60012345O"
    response = client.post('/nuevo', data= datos, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_emailIncorrecto1(client):
    datos = DATOS_CIUDADANO_BASE.copy()
    datos["correoElectronico"] = "luisexample.com"
    response = client.post('/nuevo', data=datos, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_emailIncorrecto1(client):
    datos = DATOS_CIUDADANO_BASE.copy()
    datos["correoElectronico"] = "luis@examplecom"
    response = client.post('/nuevo', data=datos, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)