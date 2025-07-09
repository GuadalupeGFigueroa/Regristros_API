import os
if not os.path.isfile(".env"):
    raise FileNotFoundError("❌ Archivo .env no encontrado. Crea uno o copia desde .env.example")

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)