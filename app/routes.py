from app import app
from flask import render_template, request, redirect, url_for, flash
from app.services.auth_service import generar_wssegpass
from app.services.soap_sedipualba import buscar_ciudadano_soap
import os
from dotenv import load_dotenv
from datetime import datetime

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
        fecha_nacimiento = request.form.get('fecha_nacimiento')

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
        fecha_nacimiento = request.form.get('fecha_nacimiento')
        telefono = request.form.get('telefono')
        correo = request.form.get('correoElectronico')
        cod_postal = request.form.get('codPostal')
        direccion_manual = request.form.get('direccion_texto')
        observaciones = request.form.get('observaciones')

        # Validación
        if not nombre or not apellido1 or not fecha_nacimiento or not telefono:
            flash("Faltan campos obligatorios.")
            return redirect(url_for('nuevo'))
        
        guardar_resultado = True #simulación de guardado

        # Llamada al servicio SOAP/REST para verificar
        respuesta = buscar_ciudadano_soap(dni, usuario=USUARIO_WSSEG, clave=CLAVE_WSSEG, entidad=ENTIDAD_CODIGO)
        if respuesta:
            fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
            datos_registro = {
                "DNI": dni,
                "Nombre": nombre, 
                "Apellidos": f"{apellido1} {apellido2}",
                "Fecha de nacimiento": fecha_nacimiento,
                "Dirección": direccion_manual,
                "Observaciones": observaciones,
                "Resultado de verificación API": respuesta
            }
            return render_template("Informe.html", datos=datos_registro, nombre=nombre, fecha=fecha)
        else:
            flash("⚠️ Hubo un problema al verificar los datos después de guardarlos.")
        return redirect(url_for('nuevo'))

        # Validar formato de fecha o normalizar
        # Validar longitud y tipo del código postal

        # Imprimir datos o enviarlos a la API
        flash("Datos del formulario recibidos correctamente. (Aún no se envían)")
        return redirect(url_for('nuevo'))
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
    return render_template("informe.html", datos=respuesta, nombre=nombre, fecha=fecha)
    return render_template('nuevo_ciudadano.html')

dni = request.form.get('dni')
nombre = request.form.get('nombre')


print("✅ routes.py cargado correctamente")

