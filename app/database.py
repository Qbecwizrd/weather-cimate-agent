# here we are going to be implementing the sqlalchemy , sqlalchemy helps to write sql queries in a  pythonic way . Also helps with object relational mapping


from sqlalchemy import create_engine # create engine is used to create a connection to the database
from sqlalchemy.ext.declarative import declarative_base # declarative base is used to create a base class for the models
from sqlalchemy.orm import sessionmaker # sessionmaker is used to create a session to interact with the database

SQLALCHEMY_DATABASE_URL = "sqlite:///./weather_app.db"  # SQLite database file

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})  # create engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # create session maker      

base = declarative_base()  # create base class for models

# tell me what this engine is used for 
# The engine is used to connect to the database. It manages the connection pool and provides a way to execute SQL statements.

