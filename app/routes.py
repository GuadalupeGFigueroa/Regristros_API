from flask import render_template, request, redirect, url_for, flash
from app.services.auth_service import generar_wssegpass
from app.services.soap_sedipualba import buscar_ciudadano_soap
import os
from dotenv import load_dotenv
from datetime import datetime
from app.db.oracle_conn import obtener_conexion
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask import Blueprint, request, jsonify

direcciones_bp = Blueprint('direcciones', __name__)

load_dotenv()

#Cargar credenciales

USUARIO_WSSEG = os.getenv('WSSEG_USER')
CLAVE_WSSEG = os.getenv('WSSEG_PASS')
ENTIDAD_CODIGO = os.getenv('WSSEG_ENTIDAD')

#Ruta de inicio
@direcciones_bp.route('/')
def index():
    return render_template('index.html')

# Buscar
@direcciones_bp.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        documentoIdentidad = request.form.get('documentoIdentidad')
        
        token = generar_wssegpass(CLAVE_WSSEG)  # según tus credenciales
        ciudadano = buscar_ciudadano_soap(
            documentoIdentidad=documentoIdentidad,
            entidad_codigo=ENTIDAD_CODIGO,  
            usuario=USUARIO_WSSEG,
            ws_segpass=token
        )

        if ciudadano:
            return render_template('ventana_resultados.html', ciudadano=ciudadano)
        else:
            flash("Ciudadano/a no encontrado")
            return redirect(url_for('direcciones.buscar'))

    return render_template('buscar.html')


@direcciones_bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo():    

    if request.method == 'POST':        
        nombre = request.form.get('nombre')
        apellido1 = request.form.get('apellido1')
        apellido2 = request.form.get('apellido2') or ''
        dni = request.form.get('dni')
        telefono = request.form.get('telefono')
        correo = request.form.get('correoElectronico')
        cod_postal = request.form.get('codPostal')
        municipio= request.form.get('municipio')
        direccion_manual = request.form.get('direccion_texto')
        observaciones = request.form.get('observaciones')

        # Validación
        if not nombre or not apellido1 or not telefono:
            flash("Faltan campos obligatorios.")
            return render_template('nuevo_ciudadano.html',
                nombre=nombre,
                apellido1=apellido1,
                apellido2=apellido2,
                telefono=telefono,
                correo=correo,
                municipio=municipio,
                observaciones=observaciones
                )
        
        guardar_resultado = True #simulación de guardado

        # Llamada al servicio SOAP/REST para verificar
        respuesta = buscar_ciudadano_soap(
            documentoIdentidad=dni,
            entidad_codigo=ENTIDAD_CODIGO,
            usuario=USUARIO_WSSEG,
            ws_segpass=CLAVE_WSSEG
        )

        if respuesta:
            fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
            datos_registro = {
                "DNI": dni,
                "Nombre": nombre, 
                "Apellidos": f"{apellido1} {apellido2}",
                "Municipio": municipio,
                "Dirección": direccion_manual,
                "Observaciones": observaciones,
                "Resultado de verificación API": respuesta
            }
            return render_template("Informe.html", datos=datos_registro, nombre=nombre, fecha=fecha)
        else:
            flash("⚠️ Hubo un problema al verificar los datos después de guardarlos.")
            return render_template("nuevo_ciudadano.html", 
                nombre=nombre, 
                apellido1=apellido1, 
                apellido2=apellido2, 
                telefono=telefono, 
                correo=correo
                )
        # 
    return render_template("nuevo_ciudadano.html")

@direcciones_bp.route('/api/vias')
def obtener_vias():
    municipio = request.args.get('municipio', '').lower()

    if municipio == 'llanera':
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            cursor.execute("SELECT nombre_via FROM vias WHERE municipio = 'Llanera'")
            resultados = [fila[0] for fila in cursor.fetchall()]
            return jsonify(resultados)
        except Exception as e:
            print(f"❌ Error al acceder a Oracle: {e}")
            return jsonify([])
        finally:
            cursor.close()
            conn.close()
    else:
        return jsonify([])
    
    # GET: mostrar formulario vacío 
    return render_template("nuevo_ciudadano.html")

# ----- Rutas para formulario de dirección -----
@direcciones_bp.route("/api/localidades", methods=["GET"])
def obtener_localidades():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM LOCALIDAD ORDER BY nombre")
        localidades = cursor.fetchall()
        return jsonify([loc[0] for loc in localidades])
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

@direcciones_bp.route("/api/tipos-via", methods=["GET"])
def obtener_tipos_via():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM TIPO_VIA ORDER BY nombre")
        tipos = cursor.fetchall()
        return jsonify([tipo[0] for tipo in tipos])
    except Exception as e: 
        return jsonify({"error": str(e)}), 500
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

@direcciones_bp.route("/api/codigos-postales", methods = ["GET"])
def obtener_codigos_postales():
    nombre_localidad = request.args.get("nombre")

    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT cp.codigo
            FROM CODIGO_POSTAL cp
            JOIN LOCALIDAD l ON cp.id_localidad = l.id_localidad
            WHERE l.nombre = : nombre_localidad
        """, [nombre_localidad])
        codigos = cursor.fetchall()
        return jsonify([c[0] for c in codigos])
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

@direcciones_bp.route("/api/via", methods=["GET"])
def obtener_via():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM VIA ORDER BY nombre")
        vias = cursor.fetchall()
        return jsonify([via[0] for via in vias])
    except Exception as e: 
        return jsonify({"error": str(e)}), 500
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()
