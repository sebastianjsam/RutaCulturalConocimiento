from src.app import db
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime, Column, Integer, \
    String, ForeignKey, JSON, Float

"""------Definicion de tablas------"""


class pueblo(db.Model):
    __tablename__ = 'pueblo'
    id = Column(Integer(), primary_key=True)
    nombre_pueblo = Column(String(), nullable=False)
    descripcion_pueblo = Column(String(), nullable=True)
    ubicacion = Column(String(), nullable=True)
    historia = Column(String(), nullable=True)
    sitio_interes = relationship("sitio_interes", back_populates="pueblo")
    eventos = relationship("eventos", back_populates="pueblo")

    def __init__(self, nombre_pueblo, descripcion_pueblo, ubicacion, historia):
        self.nombre_pueblo = nombre_pueblo
        self.descripcion_pueblo = descripcion_pueblo
        self.ubicacion = ubicacion
        self.historia = historia


class sitio_interes(db.Model):
    __tablename__ = 'sitio_interes'
    id = Column(Integer(), primary_key=True)
    nombre_sitio_interes = Column(String(), nullable=False)
    direccion_sitio_interes = Column(String(), nullable=False)
    numero_contacto = Column(String(), nullable=True)
    descripcion_sitio_interes = Column(String(), nullable=True)
    tipo_sitio = Column(JSON, nullable=False)
    historia_sitio_interes = Column(String(), nullable=True)
    pueblo_id = Column(Integer(), ForeignKey('pueblo.id'))
    pueblo = relationship("pueblo", back_populates="sitio_interes")

    def __init__(self, nombre_sitio_interes, pueblo_id, direccion_sitio_interes, numero_contacto,
                 descripcion_sitio_interes, tipo_sitio,
                 historia_sitio_interes):
        self.nombre_sitio_interes = nombre_sitio_interes
        self.pueblo_id = pueblo_id
        self.direccion_sitio_interes = direccion_sitio_interes
        self.numero_contacto = numero_contacto
        self.descripcion_sitio_interes = descripcion_sitio_interes
        self.tipo_sitio = tipo_sitio
        self.historia_sitio_interes = historia_sitio_interes


class eventos(db.Model):
    __tablename__ = 'eventos'
    id = Column(Integer(), primary_key=True)
    nombre_evento = Column(String(), nullable=False)
    fecha = Column(DateTime, nullable=False)
    descripcion_evento = Column(String(), nullable=True)
    historia = Column(String(), nullable=True)
    pueblo_id = Column(Integer(), ForeignKey('pueblo.id'))
    pueblo = relationship("pueblo", back_populates="eventos")
    actividades = relationship("actividades", back_populates="eventos")

    def __init__(self, nombre_evento, pueblo_id, fecha, descripcion_evento, historia):
        self.nombre_evento = nombre_evento
        self.pueblo_id = pueblo_id
        self.fecha = fecha
        self.descripcion_evento = descripcion_evento
        self.historia = historia


class actividades(db.Model):
    __tablename__ = 'actividades'
    id = Column(Integer(), primary_key=True)
    fecha_hora = Column(DateTime, nullable=False)
    descripcion_actividad = Column(String(), nullable=True)
    costo = Column(Float(), nullable=False)
    evento_id = Column(Integer(), ForeignKey('eventos.id'))
    eventos = relationship("eventos", back_populates="actividades")

    def __init__(self, evento_id, fecha_hora, descripcion_actividad, costo):
        self.evento_id = evento_id
        self.fecha_hora = fecha_hora
        self.descripcion_actividad = descripcion_actividad
        self.costo = costo
