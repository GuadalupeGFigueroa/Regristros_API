from app.db.oracle_conn import obtener_conexion

try:
    conn = obtener_conexion()
    cursor = conn.cursor()

    # Sustituye esta tabla por una real de tu base de datos de pruebas
    cursor.execute("""
        SELECT nombre 
        FROM VIA
        WHERE ID_LOCALIDAD = 1
    """)
    resultados = cursor.fetchall()

    print("✅ Vías encontradas en Posada:")
    for via in resultados:
        print("-", via[0])

except Exception as e:
    print("❌ Error al conectar o consultar:", e)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()