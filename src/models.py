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
    tramo = Column(String)
    fecha = Column(DateTime)
    cantidad_deudores = Column(Integer)
    total_documentos = Column(Integer)
    total_deuda = Column(Float)

class dim_tiempo(Base):
    __tablename__ = 'dim_tiempo'
    id = Column(Integer, primary_key=True)
    anno = Column(Integer) # 2010 en adelante
    mes = Column(Integer) # 1 - 12
    dia = Column(Integer) # 1 - 31
    dia_semana = Column(Integer) # 1 - 5

class fact_cliente(Base):
    __tablename__ = 'fact_cartera'
    id = Column(Integer, primary_key=True)
    cliente = Column(String)
    tipo_cartera = Column(Integer)
    promedio_deuda = Column(Float)

class fact_carteras(Base):
    __tablename__ = 'fact_cartera'
    id = Column(Integer, primary_key=True)
    cartera = Column(Integer, ForeignKey('dim_cartera.id'))
    tiempo = Column(Integer, ForeignKey('dim_tiempo.id'))
    cantidad_deudores_prom = Column(Float)
    cantidad_deuda_prom = Column(Float)
    total_deudores_nuevos = Column(Integer) # No han aparecido en previas carteras
    total_deudores_antiguos = Column(Integer) # Sin pagar o nuevos documentos
    promedio_deuda = Column(Float)  # + Campañas pasadas
    promedio_documentos = Column(Float) # + Campañas pasadas

class fact_deudor(Base): # caracteristicas de deudores
    __tablename__ = 'fact_deudor'
    id = Column(Integer, primary_key=True)
    cartera = Column(Integer, ForeignKey('dim_cartera.id'))
    tiempo = Column(Integer, ForeignKey('dim_tiempo.id'))
    


class fact_gestion(Base): # caracteristicas de gestiones
    __tablename__ = 'fact_gestion'
    id = Column(Integer, primary_key=True)
    cartera = Column(Integer, ForeignKey('dim_cartera.id'))
    tiempo = Column(Integer, ForeignKey('dim_tiempo.id'))    
    promedio_promesa = Column(Float)
    total_promesa = Column(Float)
    total_tipo1 = Column(Integer)
    promedio_tipo1 = Column(Float)
    total_tipo2 = Column(Integer)
    promedio_tipo2 = Column(Float)
    total_tipo3 = Column(Integer)
    promedio_tipo3 = Column(Float)
    total_tipo4 = Column(Integer)
    promedio_tipo4 = Column(Float)

class fact_pagos(Base): # caracteristicas de pagos
    __tablename__ = 'fact_pagos'
    id = Column(Integer, primary_key=True)
    cartera = Column(Integer, ForeignKey('dim_cartera.id'))
    tiempo = Column(Integer, ForeignKey('dim_tiempo.id'))
    promedio_pagos = Column(Float)
    pagos_total = Column(Float)
    total_deudores = Column(Integer)
    total_documentos = Column(Integer)
    promedio_deudores = Column(Integer)
    promedio_documentos = Column(Integer)


    