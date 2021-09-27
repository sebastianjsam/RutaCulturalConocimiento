from src.db.db_models import *
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, fields


class pueblo_schema(SQLAlchemySchema):
    class Meta:
        model = pueblo

    id = auto_field()
    nombre_pueblo = auto_field()
    descripcion_pueblo = auto_field()
    ubicacion = auto_field()
    historia = auto_field()


class sitio_interes_schema(SQLAlchemySchema):
    class Meta:
        model = sitio_interes

    id = auto_field()
    nombre_sitio_interes = auto_field()
    direccion_sitio_interes = auto_field()
    numero_contacto = auto_field()
    tipo_sitio = auto_field()
    historia_sitio_interes = auto_field()
    pueblo_id = auto_field()
    pueblo = fields.Nested(pueblo_schema)


class eventos_schema(SQLAlchemySchema):
    class Meta:
        model = eventos

    id = auto_field()
    nombre_evento = auto_field()
    fecha = auto_field()
    descripcion_evento = auto_field()
    historia = auto_field()
    pueblo_id = auto_field()
    pueblo = fields.Nested(pueblo_schema)

class actividades_schema(SQLAlchemySchema):
    class Meta:
        model = actividades

    id = auto_field()
    fecha_hora = auto_field()
    descripcion_actividad = auto_field()
    evento_id = auto_field()
    eventos = fields.Nested(eventos_schema)