# app/models.py

from datetime import datetime
def normalizar_fecha(fecha_str):
    """Convierte 'DD/MM/YYYY' en un objeto date"""
    try: 
        return datetime.strptime(fecha_str, '%d/%m/%Y').date()
    except ValueError:
        return None

def buscar_ciudadano(documento, fecha_nacimiento): 
    """Simula una búsqueda por documento y fecha)"""
    fecha_normalizada = normalizar_fecha(fecha_nacimiento)
    ciudadanos = [
        {
            'nombre': 'Ana García',
            'documento': '12345678A',
            'fecha_nacimiento': datetime(1985, 4, 10).date(),
            'direccion': 'Calle Mayor, 25',
        },
        {
            'nombre': 'Luis Pérez',
            'documento': 'Y1234567B',
            'fecha_nacimiento': datetime(1990, 12, 1).date(),
            'direccion': 'Avenida del Sol, 12',

        }
        #Datos simulados para hacer pruebas. Reemplazar cuando se tenga la conexión a la BBDD
    ]
    for ciudadano in ciudadanos:
        if ciudadano['documento'] == documento and ciudadano['fecha_nacimiento'] == fecha_nacimiento:
            return ciudadano # Si encuentra coincidencia
        
    return None # Si no se encuentra