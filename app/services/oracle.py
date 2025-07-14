import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

def conectar_oracle():
    try:
        user=os.getenv("ORACLE_USER")
        password=os.getenv("ORACLE_PASSWORD")
        dsn = os.getenv("ORACLE_DSN")

        conexion = oracledb.connect(user=user, password=password, dsn=dsn)
        print("✅ Conexión establecida con Oracle")
        return conexion
    except Exception as e:
        print(f"❌ Error de conexión a Oracle: {type(e).__name__} - {e}")
        return None
    
if __name__ == "__main__":
    conn = conectar_oracle()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 'OK' FROM dual")
        print(cursor.fetchone())  # resultado: ('OK',)
        cursor.close()
        conn.close() 