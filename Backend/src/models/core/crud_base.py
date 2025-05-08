# crud_base.py
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

# Definición del tipo genérico para los modelos
ModelType = TypeVar("ModelType")


class CRUDBase(Generic[ModelType]):
    """
    Clase base CRUD con operaciones predefinidas para modelos SQLAlchemy.
    """

    def __init__(self, model: Type[ModelType]):
        """
        Inicializador del CRUD.
        
        Args:
            model: Clase modelo de SQLAlchemy
        """
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        """
        Obtener un objeto por ID.
        """
        return db.query(self.model).filter(self.model.id == id).first()
        
    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[ModelType]:
        """
        Obtener múltiples objetos con paginación.
        """
        return db.query(self.model).offset(skip).limit(limit).all()
    
    def create(self, db: Session, *, obj_data: Dict[str, Any]) -> ModelType:
        """
        Crear un nuevo objeto.
        """
        try:
            db_obj = self.model(**obj_data)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        except SQLAlchemyError as e:
            db.rollback()
            raise e
    
    def update(
        self, 
        db: Session, 
        *, 
        db_obj: ModelType, 
        obj_data: Dict[str, Any]
    ) -> ModelType:
        """
        Actualizar un objeto existente.
        """
        try:
            for key, value in obj_data.items():
                if hasattr(db_obj, key):
                    setattr(db_obj, key, value)
                    
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        except SQLAlchemyError as e:
            db.rollback()
            raise e
    
    def remove(self, db: Session, *, id: Any) -> Optional[ModelType]:
        """
        Eliminar un objeto por ID.
        """
        try:
            obj = db.query(self.model).get(id)
            if obj is None:
                return None
                
            db.delete(obj)
            db.commit()
            return obj
        except SQLAlchemyError as e:
            db.rollback()
            raise e
    
    def get_by_attr(self, db: Session, attr_name: str, attr_value: Any) -> Optional[ModelType]:
        """
        Obtener un objeto por un atributo específico.
        """
        return db.query(self.model).filter(getattr(self.model, attr_name) == attr_value).first()
    
    def get_multi_by_attr(
        self, 
        db: Session, 
        attr_name: str, 
        attr_value: Any, 
        *, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[ModelType]:
        """
        Obtener múltiples objetos por un atributo específico.
        """
        return db.query(self.model).filter(
            getattr(self.model, attr_name) == attr_value
        ).offset(skip).limit(limit).all()