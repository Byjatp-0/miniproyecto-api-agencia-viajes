# API de Gestión de Clientes para Agencia de Viajes

Proyecto desarrollado por José Alberto González Muelas con FastAPI y MySQL/MariaDB para la gestión de clientes de una agencia de viajes.

---

## Características principales

* Alta, consulta, actualización y eliminación de clientes.
* Búsqueda por nacionalidad y seguro de viaje.
* Autenticación básica con JWT.
* Compatible con ejecución local y en red local (--host 0.0.0.0).
* Documentación interactiva automática generada por FastAPI en /docs.

---

## Instalación

### 1. Clonar el repositorio

git clone https://github.com/joseagm/fastapi-agencia-viajes.git
cd fastapi-agencia-viajes/backend

### 2. Crear y activar el entorno virtual

python -m venv venv
.\venv\Scripts\activate  # En Windows
# o
source venv/bin/activate  # En Linux/Mac

### 3. Instalar dependencias

pip install -r requirements.txt


### 4. Configurar base de datos (MySQL/MariaDB)

Crea una base de datos llamada agencia_viajes y edita database.py con tus credenciales:

DB_USER = "root"
DB_PASSWORD = ""
DB_HOST = "127.0.0.1"
DB_NAME = "agencia_viajes"

### 5. Crear tablas

from database import Base, engine
Base.metadata.create_all(bind=engine)


### 6. Ejecutar el servidor

uvicorn main:app --reload


---

## Acceso desde red local

Para permitir el acceso desde otros equipos en la misma red:

uvicorn main:app --host 0.0.0.0 --port 8000 --reload


Luego, acceder desde otro dispositivo:

http://<ip_local>:8000/docs


Ejemplo:

http://192.168.1.45:8000/docs

---

## Estructura del proyecto


fastapi-agencia-viajes/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── auth.py
│   └── requirements.txt
│
├── docs/
│   ├── Documentacion_Agencia_Viajes.docx
│   └── capturas/
│       ├── fastapi_docs.png
│       └── mysql_clientes.png
│
└── README.md

---

## Endpoints principales

| Método     | Ruta                                    | Descripción                         |
| ---------- | --------------------------------------- | ----------------------------------- |
| POST       | /register                               | Registrar un nuevo cliente          |
| POST       | /login                                  | Iniciar sesión y obtener token JWT  |
| GET        | /clientes/                              | Listar todos los clientes           |
| GET        | /clientes/nacionalidad/{nacionalidad}   | Buscar por nacionalidad             |
| GET        | /clientes/seguro                        | Listar clientes con seguro de viaje |
| PUT        | /clientes/{dni}                         | Actualizar datos de contacto        |
| DELETE     | /clientes/{dni}                         | Eliminar cliente                    |

---

## Autor

José Alberto González Muelas
Proyecto académico de simulación de venta — Agencia de Viajes
Grado Superior en Desarrollo de Aplicaciones Multiplataforma (DAM)
España, 2025
