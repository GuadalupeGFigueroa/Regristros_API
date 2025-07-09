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

# Tests para datos correctos
def test_nuevo_ciudadano_valido(client):
    response = client.post('/nuevo', data={
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
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Informe" in response.data
    
def test_nuevo_ciudadano_validoEspacios(client):
    response = client.post('/nuevo', data={
        "nombre": "José Luis",
        "apellido1": "Ramírez", 
        "apellido2": "Cano",
        "dni": "12345678A",

        "telefono": "600123456",
        "correoElectronico": "luis@example.com",
        "municipio": "Llanera",
        "direccion_texto": "Calle Ejemplo, 123",
        "codPostal": "33424",

        "observaciones": "Sin observaciones"
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Informe" in response.data 

def test_nuevo_ciudadano_validoApellido(client):
    response = client.post('/nuevo', data={
        "nombre": "Luis",
        "apellido1": "Del Río ", 
        "apellido2": "Cano",
        "dni": "12345678A",

        "telefono": "600123456",
        "correoElectronico": "luis@example.com",
        "municipio": "Llanera",
        "direccion_texto": "Calle Ejemplo, 123",
        "codPostal": "33424",

        "observaciones": "Sin observaciones"
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Informe" in response.data

def test_nuevo_ciudadano_validoGuiones(client):
    response = client.post('/nuevo', data={
        "nombre": "Luis",
        "apellido1": "Pérez-Gómez", 
        "apellido2": "Cano",
        "dni": "12345678A",

        "telefono": "600123456",
        "correoElectronico": "luis@example.com",
        "municipio": "Llanera",
        "direccion_texto": "Calle Ejemplo, 123",
        "codPostal": "33424",

        "observaciones": "Sin observaciones"
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Informe" in response.data

#Tests para datos incorrectos
def test_nuevo_ciudadano_nombreIncorrectoNumero(client):
    response = client.post('/nuevo', data={
        "nombre": "Lui4",
        "apellido1": "Ramírez", 
        "apellido2": "Cano",
        "dni": "12345678A",

        "telefono": "600123456",
        "correoElectronico": "luis@example.com",
        "municipio": "Llanera",
        "direccion_texto": "Calle Ejemplo, 123",
        "codPostal": "33424",

        "observaciones": "Sin observaciones"
    }, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_nombreIncorrectoSigno(client):
    response = client.post('/nuevo', data={
        "nombre": "Lui+",
        "apellido1": "Ramírez", 
        "apellido2": "Cano",
        "dni": "12345678A",

        "telefono": "600123456",
        "correoElectronico": "luis@example.com",
        "municipio": "Llanera",
        "direccion_texto": "Calle Ejemplo, 123",
        "codPostal": "33424",
        
        "observaciones": "Sin observaciones"
    }, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_apellido1IncorrectoNumero(client):
    response = client.post('/nuevo', data={
        "nombre": "Luis",
        "apellido1": "Ramíre3", 
        "apellido2": "Cano",
        "dni": "12345678A",

        "telefono": "600123456",
        "correoElectronico": "luis@example.com",
        "municipio": "Llanera",
        "direccion_texto": "Calle Ejemplo, 123",
        "codPostal": "33424",

        "observaciones": "Sin observaciones"
    }, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_apellido1IncorrectoSigno(client):
    response = client.post('/nuevo', data={
        "nombre": "Luis",
        "apellido1": "Ramíre!", 
        "apellido2": "Cano",
        "dni": "12345678A",

        "telefono": "600123456",
        "correoElectronico": "luis@example.com",
        "municipio": "Llanera",
        "direccion_texto": "Calle Ejemplo, 123",
        "codPostal": "33424",

        "observaciones": "Sin observaciones"
    }, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_apellido2IncorrectoNumero(client):
    response = client.post('/nuevo', data={
        "nombre": "Luis",
        "apellido1": "Ramírez", 
        "apellido2": "Cano6",
        "dni": "12345678A",

        "telefono": "600123456",
        "correoElectronico": "luis@example.com",
        "municipio": "Llanera",
        "direccion_texto": "Calle Ejemplo, 123",
        "codPostal": "33424",

        "observaciones": "Sin observaciones"
    }, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_apellido2IncorrectoSigno(client):
    response = client.post('/nuevo', data={
        "nombre": "Luis",
        "apellido1": "Ramírez", 
        "apellido2": "Cano+",
        "dni": "12345678A",

        "telefono": "600123456",
        "correoElectronico": "luis@example.com",
        "municipio": "Llanera",
        "direccion_texto": "Calle Ejemplo, 123",
        "codPostal": "33424",

        "observaciones": "Sin observaciones"
    }, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_teléfonoIncorrectoCorto(client):
    response = client.post('/nuevo', data={
        "nombre": "Luis",
        "apellido1": "Ramírez", 
        "apellido2": "Cano",
        "dni": "12345678A",

        "telefono": "60012345",
        "correoElectronico": "luis@example.com",
        "municipio": "Llanera",
        "direccion_texto": "Calle Ejemplo, 123",
        "codPostal": "33424",

        "observaciones": "Sin observaciones"
    }, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_teléfonoIncorrectoLargo(client):
    response = client.post('/nuevo', data={
        "nombre": "Luis",
        "apellido1": "Ramírez", 
        "apellido2": "Cano",
        "dni": "12345678A",

        "telefono": "6001234569",
        "correoElectronico": "luis@example.com",
        "municipio": "Llanera",
        "direccion_texto": "Calle Ejemplo, 123",
        "codPostal": "33424",

        "observaciones": "Sin observaciones"
    }, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_teléfonoIncorrectoLetra(client):
    response = client.post('/nuevo', data={
        "nombre": "Luis",
        "apellido1": "Ramírez", 
        "apellido2": "Cano",
        "dni": "12345678A",

        "telefono": "600123456O",
        "correoElectronico": "luis@example.com",
        "municipio": "Llanera",
        "direccion_texto": "Calle Ejemplo, 123",
        "codPostal": "33424",

        "observaciones": "Sin observaciones"
    }, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_emailIncorrecto1(client):
    response = client.post('/nuevo', data={
        "nombre": "Luis",
        "apellido1": "Ramírez", 
        "apellido2": "Cano",
        "dni": "12345678A",

        "telefono": "600123456",
        "correoElectronico": "luisexample.com",
        "municipio": "Llanera",
        "direccion_texto": "Calle Ejemplo, 123",
        "codPostal": "33424",

        "observaciones": "Sin observaciones"
    }, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)

def test_nuevo_ciudadano_emailIncorrecto2(client):
    response = client.post('/nuevo', data={
        "nombre": "Luis",
        "apellido1": "Ramírez", 
        "apellido2": "Cano",
        "dni": "12345678A",

        "telefono": "600123456",
        "correoElectronico": "luis@examplecom",
        "municipio": "Llanera",
        "direccion_texto": "Calle Ejemplo, 123",
        "codPostal": "33424",
        
        "observaciones": "Sin observaciones"
    }, follow_redirects=False)
    assert response.status_code == 200
    assert 'class="flash"' in response.get_data(as_text=True)