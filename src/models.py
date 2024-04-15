from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float,ForeignKey, DateTime, Numeric, MetaData

Base = declarative_base()

class dim_deudor(Base): # Cada deudor
    __tablename__ = 'dim_deudor'
    id = Column(Integer, primary_key=True)
    dni = Column(String)
    ruc10 = Column(String)
    ruc20 = Column(String)
    nombre = Column(String)
    apellido_pat = Column(String)
    apellido_mat = Column(String)
    nombre_completo = Column(String)
    fuente = Column(Integer)
    ubi_geo = Column(Integer)
    edad = Column(Integer)
    educacion = Column(Integer)

class dim_deuda(Base):
    __tablename__ = 'dim_deuda'
    id = Column(Integer, primary_key=True)
    num_doc = Column(Integer)
    id_deudor = Column(Integer, ForeignKey('dim_deudor.id'))
    deuda = Column(Float)
    tramo = Column(Float)
    cartera = Column(Float)
    
class dim_cartera(Base):
    __tablename__ = 'dim_cartera'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    id_cliente = Column(Integer)
    nombre_cliente = Column(String)
    fecha = Column(DateTime)
    cantidad_deudores = Column(Integer)
    total_documentos = Column(Integer)
    total_deuda = Column(Float)

class fact_cliente(Base):
    __tablename__ = 'fact_cartera'
    id = Column(Integer, primary_key=True)
    cliente = Column(String)
    tipo_cartera = Column(Integer)
    promedio_deuda = Column(Float)

class fact_carteras(Base):
    __tablename__ = 'fact_cartera'
    id = Column(Integer, primary_key=True)
    id_cartera = Column(Integer, ForeignKey('dim_cartera.id'))
    cantidad_deudores_prom = Column(Float)
    cantidad_deuda_prom = Column(Float)
    total_deudores_nuevos = Column(Integer) # No han aparecido en previas carteras
    total_deudores_antiguos = Column(Integer) # Sin pagar o nuevos documentos
    promedio_deuda = Column(Float)  # + Campañas pasadas
    promedio_documentos = Column(Float) # + Campañas pasadas

class fact_deudor(Base): # caracteristicas de deudores
    __tablename__ = 'fact_deudor'
    edad_promedio = Column(Float)
    educacion_promedio = Column(Float)
    deuda_acumulada = Column(Float)

class fact_gestion(Base): # caracteristicas de gestiones
    __tablename__ = 'fact_gestion'
    promedio_promesa = Column(Float)

class fact_pagos(Base): # caracteristicas de pagos
    __tablename__ = 'fact_pagos'
    