import requests
from config import WSSEG_USER, WSSEG_PASS, WSDL_URL 
from dotenv import load_dotenv

load_dotenv

def consultar_por_documento(documentoIdentidad):
    auth = (WSSEG_USER, WSSEG_PASS)
    try:
        response = requests.get(f"{WSDL_URL}/ciudadano/{documentoIdentidad}", auth=auth)
        response.raise_for_status()
        datos = response.json()
        if not datos:
            print("⚠️ Sin resultados.")
            return datos
    except Exception as e:
        print(f"❌ Error REST: {e}")
        return None
