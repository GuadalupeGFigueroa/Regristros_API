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

def cargar_vias_por_municipio(municipio_id, nucleo_id=None):
    try:
        conn = conectar_oracle()
        cursor = conn.cursor()
        consulta = """
            SELECT tv.TVI_DES, v.VIA_NOL, tr.TRM_CPO
            FROM ACCEDE_TER.T_VIA v
            JOIN ACCEDE_TER.T_TVI tv ON v.VIA_TVI = tv.TVI_COD
            JOIN ACCEDE_TER.T_TRM tr ON v.VIA_COD = tr.TRM_VIA
            WHERE tr.TRM_MUN = :municipio
            {filtro_nucleo}
        """
        filtro_nucleo = ""
        params = {"municipio": municipio_id}

        if nucleo_id is not None:
            filtro_nucleo = "AND tr.TRM_NUC = :nucleo"
            consulta = consulta.format(filtro_nucleo=filtro_nucleo)
            params["nucleo"] = nucleo_id
        else:
            consulta = consulta.format(filtro_nucleo="")

        cursor.execute(consulta, params)
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultados
    except Exception as e:
        print(f"❌ Error al cargar vías: {type(e).__name__} - {e}")
        return []
    # Esta función acepta un ID de municipio