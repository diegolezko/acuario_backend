🧑‍🤝‍🧑 Cómo colaborar (para tus compañeros)
1️⃣ Clonar el repositorio
git clone https://github.com/diegolezko/acuario_backend.git
cd acuario_backend

2️⃣ Crear entorno virtual
macOS / Linux
python3 -m venv venv
source venv/bin/activate

Windows
python -m venv venv
venv\Scripts\activate

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Crear la base de datos local

El proyecto usa SQLite, así que no hay que instalar ningún motor de base de datos.

Solo ejecuta:

python app/create_tables.py


Esto generará app.db y todas las tablas necesarias.

5️⃣ Ejecutar el servidor
uvicorn main:app --reload


Luego abre:

API:
http://localhost:8000

Documentación interactiva:
http://localhost:8000/docs

🔐 Autenticación

El proyecto incluye:

Registro de usuarios

Login

Generación de token JWT

Validación de credenciales

Rutas protegidas con dependencias de seguridad

📄 Archivo .gitignore recomendado

Incluido en el repo:

# Entorno virtual
venv/
env/

# Python cache
__pycache__/
*.pyc

# Base de datos local
*.db

# Variables de entorno
.env

# Config de IDE
.vscode/
.idea/

# Logs
*.log
