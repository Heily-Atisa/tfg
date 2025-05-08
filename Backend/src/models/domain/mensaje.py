from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Message(Base):
    """Modelo para mensajes de chat"""
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    id_chat = Column(Integer, ForeignKey("chats.id"))
    question = Column(String(255))
    answer = Column(Text)
    created_at = Column(DateTime(timezone=True), default=func.now())
    
    # Relaciones
    chat = relationship("Chat", back_populates="messages")