from zeep import Client
from services.simulaciones import CIUDADANOS_SIMULADOS
from config import WSDL_URL, WSSEG_USER, WSSEG_PASS

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
