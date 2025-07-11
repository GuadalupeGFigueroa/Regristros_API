import os
from dotenv import load_dotenv

load_dotenv()

WSSEG_USER = os.getenv("WSSEG_USER")
WSSEG_PASS = os.getenv("WSSEG_PASS")
WSSEG_ENTIDAD = os.getenv("WSSEG_ENTIDAD")
WSDL_URL = os.getenv("WSDL_URL")