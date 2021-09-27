from flask import jsonify
from flask_sqlalchemy import *
from sqlalchemy import *
from src.db.db_models import *
from src.app import db
from src.db_schemas.schemas import *


def crear_pueblo(request_data):
    nombre_pueblo = request_data["nombre_pueblo"]
    descripcion_pueblo = request_data["descripcion_pueblo"]
    ubicacion = request_data["ubicacion"]
    historia = request_data["historia"]

    try:
        new_pueblo = pueblo(nombre_pueblo, descripcion_pueblo, ubicacion, historia)
        db.session.add(new_pueblo)
        db.session.commit()
        mensaje = {"mensaje": "OK"}
        return mensaje

    except Exception as e:
        mensaje = {"mensaje": "no se pudo hacer comit por estas razones: " + str(e)}
        return mensaje


def crear_sitio_interes(request_data):
    nombre_sitio_interes = request_data["nombre_sitio_interes"]
    direccion_sitio_interes = request_data["direccion_sitio_interes"]
    numero_contacto = request_data["numero_contacto"]
    descripcion_sitio_interes = request_data["descripcion_sitio_interes"]
    tipo_sitio = request_data["tipo_sitio"]
    historia_sitio_interes = request_data["historia_sitio_interes"]
    pueblo_id = request_data["pueblo_id"]

    try:
        new_pueblo = sitio_interes(nombre_sitio_interes, pueblo_id, direccion_sitio_interes, numero_contacto,
                                   descripcion_sitio_interes, tipo_sitio,
                                   historia_sitio_interes)
        db.session.add(new_pueblo)
        db.session.commit()
        mensaje = {"mensaje": "OK"}
        return mensaje

    except Exception as e:
        mensaje = {"mensaje": "no se pudo hacer comit por estas razones: " + str(e)}
        return mensaje
