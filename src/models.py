from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float,ForeignKey, DateTime, Numeric, MetaData

Base = declarative_base()

class PersDeudor(Base):
    __tablename__ = "av_PersDeudor"
    nId_PersDeudor = Column(Integer, primary_key=True)
    cPers_DNI = Column(String)
    cPers_RUC = Column(String)
    cPers_ApePat = Column(String)
    cPers_ApeMat = Column(String)
    cPers_Nombres = Column(String)
    bSexo = Column(Integer)
    dFecNacimiento = Column(DateTime)
    nGra_Instruccion = Column(Integer)
    nId_Ubigeo = Column(Integer, ForeignKey())

class UbiGeo(Base):
    __tablename__ = "av_Ubigeo"
    nId_Ubigeo = Column(Integer, primary_key=True)
    nId_Provincia = Column(Integer)
    nId_Distrito = Column(Integer)
    cNombre_Ubigeo = Column(String)

class PersTelef(Base):
    __tablename__ = "av_PersTelef"
    nId_PersTelef = Column(Integer, primary_key=True)
    nId_PersDeudor = Column(Integer, ForeignKey("av_PersDeudor.nId_PersDeudor"))
    nTelef_Nro = Column(String)

class DocXCobrar(Base):
    __tablename__ = "av_DocxCobrar"
    nId_DocxCobrar = Column(Integer, primary_key=True)
    nId_Cliente = Column(Integer, ForeignKey("av_Cliente.nId_Cliente"))
    nId_Cartera = Column(Integer, ForeignKey("av_Cartera.nId_Cartera"))
    nId_PersDeudor = Column(Integer, ForeignKey("av_PersDeudor.nId_PersDeudor"))
    nDoc_ImpTotal = Column(Float)
    cPers_CodCliente = Column(Integer)

class DocXCobrarOpe(Base):
    __tablename__ = "av_DocxCobrarOpe"
    nId_DocxCobrarOpe = Column(Integer, primary_key=True)
    nId_DocxCobrar = Column(Integer, ForeignKey("av_DocxCobrar.nId_DocxCobrar"))
    nId_OpeCodIn = Column(Integer, ForeignKey(""))
    nId_UsuOpe = Column(Integer, ForeignKey(""))
    nId_PersDeudor = Column(Integer, ForeignKey("av_PersDeudor.nId_PersDeudor"))
    bOpeEfectiva = Column(Integer)
    nTelef_Nro  = Column(String)
    tip_gestion = Column(Integer, ForeignKey(""))

class Cartera(Base):
    __tablename__ = "av_Cartera"
    nId_Cartera = Column(Integer, primary_key=True)
    nId_Cliente = Column(Integer, ForeignKey(""))
    
class Cliente(Base):
    __tablename__ = "av_Cliente"
    nId_Cliente = Column(Integer, primary_key=True)
    bEstado = Column(Integer)
    nEstad_Cli_MontoSolesxCobrar = Column(Float)
    nEstad_Cli_MontoSolesRecup = Column(Float)