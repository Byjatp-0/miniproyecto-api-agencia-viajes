# crud.py
from sqlalchemy.orm import Session
from models import Clientes
from schemas import CrearCliente
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def dar_de_alta_a_cliente(db: Session, cliente: CrearCliente):
    
    db_cliente = Clientes(              
        dni=cliente.dni,
        nombre=cliente.nombre,
        apellido1=cliente.apellido1,
        apellido2=cliente.apellido2,
        direccion=cliente.direccion,
        caducidad_dni=cliente.caducidad_dni,
        fecha_nacimiento=cliente.fecha_nacimiento,
        telefono=cliente.telefono,
        nacionalidad=cliente.nacionalidad,
        seguro_viaje=cliente.seguro_viaje,
        correo_electronico=cliente.correo_electronico
    )
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def buscar_por_nacionalidad(db: Session, nacionalidad : str):
    return db.query(Clientes).filter(Clientes.nacionalidad == nacionalidad).all()

def clientes_seguro_viaje_si(db: Session):
    return db.query(Clientes).filter(Clientes.seguro_viaje == "Si").all()

def consultar_lista_completa(db: Session):
    return db.query(Clientes).all()

##En las funciones de crear, actualizar y eliminar (todo lo que no sea consultar datos) hay que usar commit para confirmar los cambios, 
# además de que se le asigna un valor para que se muestre los cambios si lo deseamos
# en eliminar cliente no se usa refresh porque lo que hace refresh es actualizar el objeto con los datos de la tabla, pero si ya no lo hay, no sirve de nada
# el db.update (no está en el ejercicio por algo) lo que hace es devolver el numero de filas afectadas, no actualiza nada, por lo tanto hay que usar el "=" a modo de setter

def eliminar_cliente(db: Session, cliente_id: int):
    cliente_eliminado = db.query(Clientes).filter(Clientes.id == cliente_id).first()
    if not cliente_eliminado:
        return None    
    db.delete(cliente_eliminado)
    db.commit()
    return cliente_eliminado

def actualizar_correo(db: Session, cliente_id: str, correo: str):
    cliente_a_actualizar = db.query(Clientes).filter(Clientes.id == cliente_id).first()
    if not cliente_a_actualizar:
        return None
    cliente_a_actualizar.correo_electronico = correo
    db.commit()
    db.refresh(cliente_a_actualizar)
    return cliente_a_actualizar

