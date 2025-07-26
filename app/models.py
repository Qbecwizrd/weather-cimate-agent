# here we are going to create the database and the tables

from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database import base  # Import the base from database.py

class JournalEntry(base):
    __tablename__ = "journal_entries"  # Name of the table in the database

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    location = Column(String, index=True)
    temperature = Column(Float, nullable=True)
    description = Column(String)

