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

class dim_ubigeo(Base):
    __tablename__ = 'dim_ubigeo'
    id = Column(Integer, primary_key=True)
    pais = Column(String)
    departamento = Column(String)
    provincia = Column(String)
    distrito = Column(String)
    nombre = Column(String)

class dim_telefonos(Base):
    __tablename__ = "dim_telefono"
    id = Column(Integer, primary_key=True)
    id_deudor = Column(Integer, ForeignKey("dim_deudor.id"))
    nTelef_Nro = Column(String)

class dim_deuda(Base):
    __tablename__ = 'dim_deuda'
    id = Column(Integer, primary_key=True)
    num_doc = Column(Integer)
    deudor = Column(Integer, ForeignKey('dim_deudor.id'))
    deuda = Column(Float)
    tramo = Column(Float)
    cartera = Column(Integer, ForeignKey('dim_cartera'))
    
class dim_cartera(Base):
    __tablename__ = 'dim_cartera'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    cliente = Column(Integer, ForeignKey('dim_cliente.id'))
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

class dim_cliente(Base):
    __tablename__ = 'dim_cliente'
    id = Column(Integer, primary_key=True)
    cliente = Column(String)

class fact_carteras(Base):
    __tablename__ = 'fact_cartera'
    id = Column(Integer, primary_key=True)
    cliente = Column(Integer, ForeignKey('dim_cliente.id'))
    cartera = Column(Integer, ForeignKey('dim_cartera.id'))
    tiempo = Column(Integer, ForeignKey('dim_tiempo.id'))
    cantidad_deudores_prom = Column(Float)
    cantidad_deuda_prom = Column(Float)
    total_deudores_nuevos = Column(Integer) # No han aparecido en previas carteras
    total_deudores_antiguos = Column(Integer) # Sin pagar o nuevos documentos
    total_deudores = Column(Integer) # SUMA
    promedio_deuda = Column(Float)  # + Campañas pasadas
    deuda_total = Column(Float)
    total_documentos = Column(Integer)
    promedio_documentos = Column(Float) # + Campañas pasadas
    
class fact_deudor(Base): # caracteristicas de deudores 
    __tablename__ = 'fact_deudor'
    id = Column(Integer, primary_key=True)
    deudor = Column(Integer, ForeignKey('dim_deudor.id'))
    cartera = Column(Integer, ForeignKey('dim_cartera.id'))
    tiempo = Column(Integer, ForeignKey('dim_tiempo.id'))
    ubigeo = Column(Integer, nullable=True)
    cant_compras = Column(Integer)
    cant_deuda = Column(Float)
    cant_pago = Column(Float)
    compra_promedio = Column(Float)
    cant_promesas = Column(Float)
    cant_gestiones = Column(Integer)

class fact_ubigeo(Base):
    __tablename__ = 'fact_ubigeo'
    id = Column(Integer, primary_key=True)
    ubigeo = Column(Integer, ForeignKey('dim_ubigeo.id'))
    cartera = Column(Integer, ForeignKey('dim_cartera.id'))
    total_deudores = Column(Integer)

class fact_clientes(Base):
    __tablename__ = 'fact_cliente'
    id = Column(Integer, primary_key=True)
    cliente = Column(Integer, ForeignKey('dim_cliente.id'))
    total_carteras = Column(Integer)
    total_deuda = Column(Float)
    total_recuperado = Column(Float)
    

class fact_promesa(Base):
    __tablename__ = 'fact_promesa'
    id = Column(Integer, primary_key=True)
    cartera = Column(Integer, ForeignKey('dim_cartera.id'))
    tiempo = Column(Integer, ForeignKey('dim_tiempo.id'))
    promesas_total = Column(Integer)
    porcentaje_promesa = Column(Float) # De numero de gestiones por campaña cuantas promesas
    porcentaje_promesas_cumplidas = Column(Float) 
    porcentaje_promesas_sin_cumplir = Column(Float)
    
class fact_gestion(Base): # caracteristicas de gestiones
    __tablename__ = 'fact_gestion'
    id = Column(Integer, primary_key=True)
    cartera = Column(Integer, ForeignKey('dim_cartera.id'))
    tiempo = Column(Integer, ForeignKey('dim_tiempo.id'))
    gestiones_total = Column(Integer)
    promedio_numeros_deudor = Column(Integer) #numeros de telefono de deudor
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
    