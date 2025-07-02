from flask import Flask
from flask import Blueprint

app = Flask(__name__)
app.secret_key = 'clave_secreta_123'  

from app.routes import direcciones_bp
app.register_blueprint(direcciones_bp)