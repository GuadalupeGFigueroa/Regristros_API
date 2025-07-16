from flask import Blueprint, request, jsonify
from app.services.oracle import cargar_vias_por_municipio

vias_bp = Blueprint('vias_bp', __name__)

@vias_bp.route("/vias", methods=["GET"])
def obtener_vias():
    municipio = request.args.get("municipio")
    nucleo = request.args.get("nucleo")

    if not municipio:
        return jsonify({"error": "⚠️ Falta parámetro municipio"}), 400
    try: 
        vias = cargar_vias_por_municipio(int(municipio), int(nucleo) if nucleo else None)
        datos = [
            {
                "tipo_via": v[0],
                "nombre_via": v[1],
                "cod_postal": v[2]
            }
            for v in vias
        ]
        return jsonify(datos)
    except Exception as e: 
        print(f"❌ Error en obtener_vias: {type(e).__name__} - {e}")
        return jsonify({"error":"❌ Error interno al consultar las vías"}), 500