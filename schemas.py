from pydantic import BaseModel
from datetime import date

## Aquí se definen cómo los datos entran y salen por tu API.
    
class CrearCliente(BaseModel):
    dni: str
    nombre: str
    apellido1: str
    apellido2: str
    direccion: str
    caducidad_dni: date
    fecha_nacimiento: date
    telefono: str
    nacionalidad: str
    seguro_viaje: str
    correo_electronico: str

    class Config:
        from_attributes = True #Esto evita que salga un error en la terminal que dice que el objeto no está mapeado, osea, que no lo entiende el conversor de la api con python

## Aquí devuelve al usuario pero con el id también 
class RespuestaCliente(CrearCliente):
    id : int

