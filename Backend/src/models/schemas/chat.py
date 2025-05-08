from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime

class ChatBase(BaseModel):
    name_chat: str
    
    @validator('name_chat')
    def name_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('el nombre del chat no puede estar vacío')
        return v

class ChatCreate(ChatBase):
    pass

class ChatMessage(BaseModel):
    id: Optional[int] = None
    id_chat: int
    question: str
    answer: Optional[str] = None
    created_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class ChatResponse(ChatBase):
    id: int
    id_user: int
    created_at: Optional[datetime] = None
    messages: Optional[List[ChatMessage]] = []
    
    class Config:
        from_attributes = True