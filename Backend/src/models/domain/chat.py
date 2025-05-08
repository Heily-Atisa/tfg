from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Chat(Base):
    """Modelo para chats del sistema"""
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("users.id"))
    name_chat = Column(String(255))
    created_at = Column(DateTime(timezone=True), default=func.now())
    
    # Relaciones
    user = relationship("User", back_populates="chats")
    messages = relationship("Message", back_populates="chat")