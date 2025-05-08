from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class DocumentAccess(Base):
    """Modelo para acceso a documentos por usuario"""
    __tablename__ = "acceso_documentos_usuario"

    id_document = Column(Integer, ForeignKey("documents.id"), primary_key=True)
    id_user = Column(Integer, ForeignKey("users.id"), primary_key=True)
    linked_time = Column(DateTime(timezone=True), default=func.now())
