# 🚀 Mi API con FastAPI - Python

API REST construida con **FastAPI** y **Python** como parte del proyecto formativo ADSO-3278641-4T.

---

## 📁 Estructura del proyecto

```
mi-api-fastapi-python/
├── app/
│   └── main.py          # Código principal de la API
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Este archivo
```

---

## ⚙️ Requisitos previos

- Python 3.10 o superior
- pip

---

## 🛠️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/mi-api-fastapi-python.git
cd mi-api-fastapi-python
```

### 2. Crear y activar el entorno virtual

**Windows (PowerShell):**
```powershell
python -m venv venv
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

**Linux / Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Levantar el servidor

```bash
uvicorn app.main:app --reload
```

El servidor quedará corriendo en: **http://127.0.0.1:8000**

---

## 📌 Endpoints disponibles

| Método | Ruta               | Descripción                              |
|--------|--------------------|------------------------------------------|
| GET    | `/`                | Retorna un mensaje de bienvenida         |
| GET    | `/items/{item_id}` | Retorna un ítem por ID (query `q` opcional) |

### Ejemplos de uso

```
GET http://127.0.0.1:8000/
→ {"message": "Hola mundo. Te saludo desde FastAPI"}

GET http://127.0.0.1:8000/items/9
→ {"item_id": 9, "q": null}

GET http://127.0.0.1:8000/items/9?q=SmartTV
→ {"item_id": 9, "q": "SmartTV"}
```

---

## 📄 Documentación interactiva

FastAPI genera documentación automática:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

---

## 🧪 Pruebas

Puedes probar la API con:
- Navegador web
- [Postman](https://www.postman.com/)
- Swagger UI (incluido en la app)
- `curl`:

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/items/9?q=SmartTV
```

---

## 🏷️ Versión

`v1.0.0` — API base con endpoints de ejemplo funcionales.
