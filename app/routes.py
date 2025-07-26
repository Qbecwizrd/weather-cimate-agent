# Here we define the routes for our FastAPI application.

from fastapi import APIRouter, Depends, HTTPException

# wat does depends do?
# Depends is a FastAPI dependency injection system that allows you to define dependencies for your route handlers.
# It is used to inject dependencies such as database sessions, authentication, or other services into your route functions.
# In this case, it is used to inject the database session into the route handlers.
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal
from app.models import JournalEntry

# Create a new APIRouter instance
router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/entries", response_model=schemas.JournalEntryRead)
def create_journal_entry(entry: schemas.JournalEntryCreate, db: Session = Depends(get_db)):
    """
    Create a new journal entry.
    """
    return crud.create_journal_entry(db=db, entry=entry)

@router.get("/entries", response_model=list[schemas.JournalEntryRead])
def read_journal_entries(skip: int = 0, limit: int = 100,
                        db: Session = Depends(get_db)):
    """
    Retrieve journal entries with pagination.
    """
    entries = crud.get_journal_entries(db=db, skip=skip, limit=limit)
    return entries


