import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app.services.soap_sedipualba import buscar_ciudadano_soap

def test_ciudadano_existente_laura():
    resultado = buscar_ciudadano_soap("12345678A", "EntidadDemo", "usuario", "clave")
    assert resultado is not None
    assert resultado["nombre"] == "Laura"
    assert resultado["direccion"] == "Calle Ficticia, 10"

def test_ciudadano_existente_javier():
    resultado = buscar_ciudadano_soap("87654321Z", "EntidadDemo", "usuario", "clave")
    assert resultado is not None
    assert resultado["apellido1"] == "Gómez"

def test_ciudadano_existente_ana():
    resultado = buscar_ciudadano_soap("11223344X", "EntidadDemo", "usuario", "clave")
    assert resultado is not None
    assert resultado["telefono"].startswith("620")

def test_ciudadano_inexistente():
    resultado = buscar_ciudadano_soap("00000000X", "EntidadDemo", "usuario", "clave")
    assert resultado is None