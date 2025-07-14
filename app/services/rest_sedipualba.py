import requests
from config import REST_URL, REST_USER, REST_PASS
from dotenv import load_dotenv

load_dotenv

def consultar_por_documento(documentoIdentidad):
    auth = (REST_USER, REST_PASS)
    url = f"{REST_URL}/getByDocumento/{documentoIdentidad}"
    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        datos = response.json()
        if not datos:
            print("⚠️ Sin resultados.")
            return datos
    except Exception as e:
        print(f"❌ Error REST: {type(e).__name__}: {e}")
        return None
