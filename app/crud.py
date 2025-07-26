# here we are goign to define the CRUD operations for our app
from sqlalchemy.orm import Session # Import Session for database operations
from app.models import JournalEntry  # Import the journalEntry model table
from app.schemas import JournalEntryCreate, JournalEntryRead  # Import Pydantic schemas for validation
from app import models, schemas  # Import models and schemas from the current package



# Function to create a new journal entry
def create_journal_entry(db: Session, entry: schemas.JournalEntryCreate):
    new_entry = models.JournalEntry(
        location=entry.location,
        temperature=entry.temperature,
        description=entry.description
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

def get_journal_entries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.JournalEntry).offset(skip).limit(limit).all()