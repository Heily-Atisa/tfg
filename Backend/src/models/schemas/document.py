from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime

class DocumentBase(BaseModel):
    title: str
    
    @validator('title')
    def title_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('el título no puede estar vacío')
        return v

class DocumentCreate(DocumentBase):
    # Campos adicionales que podrían ser necesarios al crear un documento
    pass

class DocumentResponse(DocumentBase):
    id: int
    chromadb_id: str
    uploaded_by: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True  # versión actualizada de orm_mode