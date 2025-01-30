from typing import TypeVar
from sqlalchemy.orm import DeclarativeBase

class _BaseType(DeclarativeBase):
    pass

DeclarativeBaseClass = TypeVar("T", bound= _BaseType)
