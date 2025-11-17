⚙️ Instalación
1️⃣ Clonar el repositorio
git clone https://github.com/diegolezko/acuario_backend.git
cd acuario_backend

2️⃣ Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # En Mac/Linux
venv\Scripts\activate     # En Windows

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Configurar variables de entorno

Crea un archivo .env en la raíz:

DATABASE_URL=mysql+mysqlconnector://usuario:password@localhost:3306/acuario
SECRET_KEY=tu_llave_secreta
ALGORITHM=HS256

▶️ Ejecutar el servidor
uvicorn app.main:app --reload


El backend se abrirá en:
👉 http://localhost:8000

Documentación interactiva:
👉 http://localhost:8000/docs
