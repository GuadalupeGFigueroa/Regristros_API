from zeep import Client

    #Código para hacer pruebas en local simulando datos
def buscar_ciudadano_soap(documentoIdentidad, entidad_codigo, usuario, ws_segpass):
    if documentoIdentidad == "12345678A":
        return {
            "nombre": "Laura Martínez",
            "apellido1": "Martínez",
            "apellido2": "Pérez",
            "nif": "12345678A",
            "fechaNacimiento": "1992-08-12",
            "telefono": "600123456",
            "correoElectronico": "laura@example.com",
            "direccion": "Calle Ficticia, 10"
        }
    else:
        return None

# Código comentado para hacer conexión real 
"""
def buscar_ciudadano_soap(documentoIdentidad, entidad_codigo, usuario, ws_segpass):
    wsdl_url = f'https://<CODIGO_ENTIDAD>.sedipualba.es/seres/Servicios/wsseresciudadano.asmx?WSDL'
    client = Client(wsdl=wsdl_url)
    
    respuesta = client.service.GetCiudadanoBydocumentoIdentidad(
        wsSegUser=usuario,
        wsSegPass=ws_segpass,
        wsEntidad=entidad_codigo,
        documentoIdentidad=documentoIdentidad
    )
    return respuesta
"""