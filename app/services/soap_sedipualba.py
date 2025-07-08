from zeep import Client

MODO_SIMULACION = True

# Código para hacer pruebas en local simulando datos
# Cambiar MODO_SIMULACION = False para pasar a producción sin modificar el resto del código.


def buscar_ciudadano_soap(documentoIdentidad, entidad_codigo, usuario, ws_segpass):
    if MODO_SIMULACION:
        simulados = {
            "12345678A": {
                "nombre": "Laura",
                "apellido1": "Martínez",
                "apellido2": "Pérez",
                "nif": "12345678A",
                "fechaNacimiento": "1992-08-12",
                "telefono": "600123456",
                "correoElectronico": "laura@example.com",
                "direccion": "Calle Ficticia, 10"
            },
            "87654321Z": {
                "nombre": "Javier",
                "apellido1": "Gómez",
                "apellido2": "Ruiz",
                "nif": "87654321Z",
                "fechaNacimiento": "1985-04-22",
                "telefono": "699987654",
                "correoElectronico": "javier@example.com",
                "direccion": "Avenida Prueba, 22"
            },
            "11223344X": {
                "nombre": "Ana",
                "apellido1": "Santos",
                "apellido2": "Moreno",
                "nif": "11223344X",
                "fechaNacimiento": "1978-11-02",
                "telefono": "620112233",
                "correoElectronico": "ana@example.com",
                "direccion": "Calle Ensayo, 5"
            }
        }
        print(f"🧪 Mock SEDIPUALBA: DNI recibido {documentoIdentidad}")
        return simulados.get(documentoIdentidad, None)
    else:
        wsdl_url = f'https://<CODIGO_ENTIDAD>.sedipualba.es/seres/Servicios/wsseresciudadano.asmx?WSDL'
        client = Client(wsdl=wsdl_url)
        
        respuesta = client.service.GetCiudadanoBydocumentoIdentidad(
            wsSegUser=usuario,
            wsSegPass=ws_segpass,
            wsEntidad=entidad_codigo,
            documentoIdentidad=documentoIdentidad
        )
        return respuesta
