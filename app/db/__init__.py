from .oracle_conn import obtener_conexion

from flask import Flask
from app.vias import vias_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(vias_bp)
    return app