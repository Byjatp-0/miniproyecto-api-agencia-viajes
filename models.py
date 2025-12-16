from sqlalchemy import Column, Integer, String, Date, Enum
from database import Base


class Clientes(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    dni = Column(String(9))
    nombre = Column(String(50), index=True)
    apellido1 = Column(String(50), nullable=False)
    apellido2 = Column(String(50), nullable=False)
    direccion = Column(String(150), nullable=False)
    caducidad_dni = Column(Date, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    telefono = Column(String(16))
    nacionalidad = Column(String(50), nullable=False, index=True)
    seguro_viaje = Column(Enum("SI", "NO"), nullable=False, index=True)
    correo_electronico = Column(String(100), unique=True, index=True)