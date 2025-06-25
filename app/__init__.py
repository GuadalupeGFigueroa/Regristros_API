from flask import Flask

app = Flask(__name__)
app.secret_key = 'clave_secreta_123'  

from app import routes  # ¡IMPORTANTE! Debe estar al final