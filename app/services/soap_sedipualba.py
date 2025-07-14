from zeep import Client
from app.services.simulaciones import CIUDADANOS_SIMULADOS
from config import WSDL_URL, WSSEG_USER, WSSEG_PASS, WSSEG_ENTIDAD

MODO_SIMULACION = True

# Cambiar MODO_SIMULACION = False para pasar a producción sin modificar el resto del código.


def buscar_ciudadano_soap(documentoIdentidad, entidad_codigo, usuario, ws_segpass):
    if MODO_SIMULACION:
        return CIUDADANOS_SIMULADOS.get(documentoIdentidad, None)
    else:
        try:
            client = Client(wsdl=WSDL_URL)
            respuesta = client.service.GetCiudadanoBydocumentoIdentidad(
                wsSegUser=usuario,
                wsSegPass=ws_segpass,
                wsEntidad=entidad_codigo,
                documentoIdentidad=documentoIdentidad
            )
            return respuesta
        except Exception as e: 
            print(f" ❌ Error SOAP: {e}")
            return None
        
def probar_conexion_sedipualba():
    try:
        client = Client(wsdl=WSDL_URL)

        respuesta = client.service.GetCiudadanoBydocumentoIdentidad(
            wsSegUser=WSSEG_USER,
            wsSegPass=WSSEG_PASS,
            wsEntidad=WSSEG_ENTIDAD,
            documentoIdentidad="12345678A" #DNI válido para la prueba
    )

        print("✅ Conexión exitosa con SEDIPUALBA")
        print("Resuktado:", respuesta)
        return True
    
    except Exception as e: 
        print(f"❌ Error de conexión con SEDIPUALBA: {type(e).__name__}")
        print("Detalles:", e)
        return False
