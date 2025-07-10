import requests
from config import WSSEG_USER, WSSEG_PASS, WSDL_URL 

from dotenv import load_dotenv

load_dotenv

def consultar_por_documento(documento):
    auth = (WSSEG_USER, WSSEG_PASS)
    url = WSDL_URL  
    try:
        response = requests.get(f"{url}/ciudadano/{documento}", auth=auth)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ Error REST: {e}")
        return None
