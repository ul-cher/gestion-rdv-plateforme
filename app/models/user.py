from sqlalchemy import Column, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class UserRole(str, enum.Enum):
    CLIENT = "client"
    PROFESSIONAL = "professional"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    role = Column(Enum(UserRole), default=UserRole.CLIENT)
    is_active = Column(Boolean, default=True)
    phone = Column(String, nullable=True)
    
    appointments_as_client = relationship("Appointment", 
        foreign_keys="Appointment.client_id", back_populates="client")
    appointments_as_professional = relationship("Appointment", 
        foreign_keys="Appointment.professional_id", back_populates="professional")
    availabilities = relationship("Availability", back_populates="professional")