import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

# Datos de conexión desde .env

USER = os.getenv("ORACLE_USER")
PASSWORD = os.getenv("ORACLE_PASSWORD")
DNS = os.getenv("ORACLE_DNS") # Puede ser host: puerto/servicio

try:
    conn = oracledb.connect(user=USER, password=PASSWORD, dns=DNS)
    cursor = conn.cursor()
    cursor.execute("SELECT 'Conexión OK desde Flask + oracledb' FROM dual")
    print(cursor.fetchone()[0])
except Exception as e:
    print("❌ Error al conectar:", e)
finally:
    cursor.close()
    conn.close()


def obtener_conexion():
    return oracledb.connect(user=USER, password=PASSWORD, dns=DNS)