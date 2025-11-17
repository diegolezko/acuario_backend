from database import Base, engine
from models import User

print("🔧 Creando tablas en la base de datos MySQL...")

# Crea todas las tablas definidas en los modelos
Base.metadata.create_all(bind=engine)

print("✅ Tablas creadas correctamente.")
