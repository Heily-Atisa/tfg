from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, DateTime, String
from datetime import datetime
from typing import Any, Dict
from sqlalchemy.orm import Session

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        """Convert model instance to dictionary."""
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BaseModel":
        """Create model instance from dictionary."""
        return cls(**data)
        
    def update_from_dict(self, data: Dict[str, Any], db: Session) -> None:
        """Update model instance from dictionary."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        db.add(self)
        db.commit()
        db.refresh(self)
