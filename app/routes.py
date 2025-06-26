from app import app
from flask import render_template, request, redirect, url_for, flash
from app.services.auth_service import generar_wssegpass
from app.services.soap_sedipualba import buscar_ciudadano_soap
import os
from dotenv import load_dotenv
from datetime import datetime
from app.db.oracle_conn import obtener_conexion
from flask import render_template, request, redirect, url_for, flash, jsonify

load_dotenv()

#Cargar credenciales

USUARIO_WSSEG = os.getenv('WSSEG_USER')
CLAVE_WSSEG = os.getenv('WSSEG_PASS')
ENTIDAD_CODIGO = os.getenv('WSSEG_ENTIDAD')

#Ruta de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Buscar
@app.route('/buscar', methods=['GET', 'POST'])
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
            return redirect(url_for('buscar'))

    return render_template('buscar.html')


@app.route('/nuevo', methods=['GET', 'POST'])
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
            return render_template(url_for('nuevo_ciudadano.html',
                nombre=nombre,
                apellido1=apellido1,
                apellido2=apellido2,
                telefono=telefono,
                correo=correo,
                municipio=municipio,
                observaciones=observaciones
                ))
        
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

@app.route('/api/vias')
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

