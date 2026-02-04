from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, appointments, users
from app.database import engine, Base
from app.config import get_settings

settings = get_settings()

# Créer les tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Appointment Platform API",
    description="API de gestion de rendez-vous",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(appointments.router, prefix="/api/appointments", tags=["Appointments"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de gestion de rendez-vous"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}