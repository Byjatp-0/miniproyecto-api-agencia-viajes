# main.py
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from schemas import *
import crud, schemas, models

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gestión de clientes")

# Dependencia para obtener la sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

## Estos aquí donde los ves, son los endpoints, se caracterizan por tener un decorador (post, get, delete, put), que indican el tipo de petición:
## Get para consultas de tipo Select
## Post para consultas Insert
## Delete para consulas Delete
## Put para consultas de tipo Update (1)

## Dentro de los paréntesis de cada decorador se pone la ruta de la api a la cual vamos a hacer esa consulta (1)

## El response model es el esquema de datos que devolverá el endpoint, por ejemplo ClienteResponse devuelve todos los datos del cliente, 
# y si queremos una lista de los clientes pondremos [ClienteResponse] (1)

## Luego dentro de la función el db: Session indica la sesión de la base de datos y el depends es para la ejecucioón de la función automáticamente (2)
## Si para nuestra función necesitamos también algún parámetro pues se lo ponemos también, 
# además de que en el primer caso, CrearCliente es el tipo de estructura que debe seguir según lo indicado en los schemas(2)

## Luego llamamos a la función CRUD que hace las operaciones en la base de datos, si encuentra algo pues devuelve error con mensaje de error (3)

## Usar {} es para un input y tienen que tener el mismo nombre que el parámetro de la función de abajo y / es para ruta



@app.post("/clientes", response_model=RespuestaCliente) #(1)
def crear_cliente(cliente: CrearCliente, db: Session = Depends(get_db)): #(2)
    existe = False
    if db.query(models.Clientes).filter(models.Clientes.dni == cliente.dni).first() or db.query(models.Clientes).filter(models.Clientes.correo_electronico == cliente.correo_electronico).first():
        existe = True #(3)
    if existe:
        raise HTTPException(status_code=400, detail="El usuario ya existe")   
    return crud.dar_de_alta_a_cliente(db, cliente)

# Rutas específicas ANTES de rutas con parámetros
@app.get("/clientes/seguro_viaje", response_model=list[RespuestaCliente])
def clientes_seguro_viaje_si(db: Session = Depends(get_db)):
    clientes_con_seguro = crud.clientes_seguro_viaje_si(db)
    if not clientes_con_seguro:
        raise HTTPException(status_code=404, detail="No hay usuarios con seguro")
    return clientes_con_seguro

@app.get("/clientes", response_model=list[RespuestaCliente])
def listar_todos_los_usuarios(db: Session = Depends(get_db)):
    lista_usuarios = crud.consultar_lista_completa(db)
    if not lista_usuarios:
        raise HTTPException(status_code=404, detail="No hay usuarios registrados")
    return lista_usuarios

# Ruta con parámetro AL FINAL
@app.get("/clientes/{nacionalidad}", response_model=list[RespuestaCliente])
def obtener_usuarios_por_nacionalidad(nacionalidad: str, db: Session = Depends(get_db)):
    clientes_encontrados = crud.buscar_por_nacionalidad(db, nacionalidad)
    if not clientes_encontrados:
        raise HTTPException(status_code=404, detail=f"No se encontraron clientes con la nacionalidad {nacionalidad}")
    return clientes_encontrados

@app.delete("/clientes/{cliente_id}")
def eliminar_usuario(cliente_id: int, db: Session = Depends(get_db)):
    usuario_a_eliminar = crud.eliminar_cliente(db, cliente_id)
    if not usuario_a_eliminar:
        raise HTTPException(status_code=404, detail="No se ha encontrado al usuario")
    return {"mensaje": f"Se eliminó al usuario con ID {cliente_id}"} 

@app.put("/clientes/{cliente_id}")
def actualizar_correo_electronico(
    cliente_id: int, 
    correo: str = Query(..., description="Nuevo correo del cliente"), 
    db: Session = Depends(get_db)
):
    usuario_correo = crud.actualizar_correo(db, cliente_id, correo)
    if not usuario_correo:
        raise HTTPException(status_code=404, detail="No se encuentra al usuario")
    return {"mensaje": f"Se actualizó el correo a {correo}"}  # Corrección de sintaxis