import hashlib
import base64
from datetime import datetime

def generar_wssegpass(clave_clara: str) -> str:
    """
    Genera el wsSegPass requerido por los servicios SOAP de SEDIPUALBA.
    
    Parámetros:
        clave_clara (str): La clave proporcionada por la entidad en texto plano.
    
    Retorna:
        str: El token wsSegPass válido.
    """
    # Obtener la hora UTC actual en formato requerido: yyyyMMddHHmmss
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')

    # Concatenar timestamp con la clave clara
    texto_para_hashear = f"{timestamp}{clave_clara}"

    # Codificar en UTF-8 y calcular hash SHA256
    hash_bytes = hashlib.sha256(texto_para_hashear.encode('utf-8')).digest()

    # Convertir el hash a Base64
    hash_base64 = base64.b64encode(hash_bytes).decode('utf-8')

    # Devolver el wsSegPass final: timestamp + hash codificado
    return f"{timestamp}{hash_base64}"