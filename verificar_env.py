import os 

""" Se crea este scrip para avisar si vuelve a borrarse de forma no intencionada 
el archivo .env al hacer controles de versiones u otras acciones. """
# Se ejecuta con run.py o con: python verificar_env.py && python run.py


def verificar_env():
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if not os.path.isfile(env_path):
        print("⚠️  Archivo .env no encontrado.")
        print("👉 Crea uno en la raíz del proyecto o copia desde .env.example")
        return False
    print("✅ Archivo .env detectado.")
    return True

if __name__ == "__main__":
    if not verificar_env():
        exit(1)

