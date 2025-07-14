import os
from app.services.soap_sedipualba import probar_conexion_sedipualba
from app import create_app

if not os.path.isfile(".env"):
    raise FileNotFoundError("❌ Archivo .env no encontrado. Crea uno o copia desde .env.example")


app = create_app()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
    probar_conexion_sedipualba()