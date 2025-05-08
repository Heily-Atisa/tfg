from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    
    @validator('username')
    def username_alphanumeric(cls, v):
        if not v.isalnum():
            raise ValueError('debe contener solo caracteres alfanuméricos')
        return v

class UserCreate(UserBase):
    password: str
    
    @validator('password')
    def password_min_length(cls, v):
        if len(v) < 8:
            raise ValueError('debe tener al menos 8 caracteres')
        return v

class UserResponse(UserBase):
    id: int
    is_admin: bool = False
    
    class Config:
        orm_mode = True