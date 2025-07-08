from flask import Flask
from flask import Blueprint
from app.routes import direcciones_bp


def create_app():
    app = Flask(__name__)
    app.secret_key = 'clave_secreta_123'  
    
    app.register_blueprint(direcciones_bp)
    return app