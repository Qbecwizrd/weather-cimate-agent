from fastapi import FastAPI
from app.database import SessionLocal, engine, base
from app.routes import router as journal_router
from climate_agent.routes import router as climate_router  # 👈 NEW IMPORT

app = FastAPI()

base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Weather Journal API!"}

# Include routers
app.include_router(journal_router)         # 📘 Existing journal routes
app.include_router(climate_router)         # 🌤️ Climate agent routes
