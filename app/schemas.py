# here will create the schemas for the application

from pydantic import BaseModel # Pydantic is used for data validation and serialization
from datetime import datetime # Import datetime for date handling
from typing import Optional # Optional is used for optional fields in Pydantic models


class JournalEntryBase(BaseModel):
    location: str
    temperature: Optional[float] = None  # Temperature is optional
    description: str

class JournalEntryCreate(JournalEntryBase):
    pass  # This model is used for creating new journal entries

class JournalEntryRead(JournalEntryBase):
    id: int  # ID is required for reading entries
    date : datetime  # Date is required for reading entries
    class Config:
        orm_mode = True  # This allows Pydantic to work with SQLAlchemy models
        # orm_mode=True tells Pydantic to treat the SQLAlchemy model as a dictionary
        # This is necessary for returning SQLAlchemy models in the response