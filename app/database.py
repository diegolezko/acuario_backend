from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión para MySQL
# Formato: mysql+pymysql://usuario:contraseña@host/base_de_datos
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://diego:123456@localhost/acuario_db"

# Crear el engine (no uses connect_args con MySQL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Dependencia para obtener una sesión de BD en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
