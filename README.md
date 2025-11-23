# 🏢 Corporate Information API

API REST que proporciona información corporativa sobre políticas internas, procedimientos administrativos y directorio de contactos de la empresa.

## 📋 Descripción

Esta API simula un sistema de información corporativa que permite consultar:
- **Políticas internas**: vacaciones, teletrabajo, código de ética, reembolsos, etc.
- **Procedimientos administrativos**: solicitud de vacaciones, reembolsos, equipos de TI, etc.
- **Directorio de contactos**: información de departamentos como RRHH, TI, Finanzas, etc.

## 🚀 Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```powershell
   cd c:\MISO\LLMs\Sem6-Agente\corporate-api
   ```

2. **Crear un entorno virtual (recomendado)**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```powershell
   pip install -r requirements.txt
   ```

## ▶️ Ejecución

### Iniciar el servidor

```powershell
python main.py
```

El servidor estará disponible en: **http://localhost:8002**

### Ejecución con Uvicorn (alternativa)

```powershell
uvicorn main:app --host 0.0.0.0 --port 8002 --reload
```

## 📚 Documentación de la API

### URL Base
```
http://localhost:8002
```

### Documentación Interactiva

Una vez el servidor esté ejecutándose, puedes acceder a la documentación interactiva en:
- **Swagger UI**: http://localhost:8002/docs
- **ReDoc**: http://localhost:8002/redoc

## 🔌 Endpoints Disponibles

### 1. **Información General**

#### GET `/`
Información sobre la API y sus endpoints disponibles.

**Respuesta:**
```json
{
  "service": "Corporate Information API",
  "version": "1.0.0",
  "description": "Sistema de información corporativa",
  "endpoints": {
    "policies": "/api/policies/{category}",
    "procedures": "/api/procedures/{name}",
    "contacts": "/api/contacts/{department}",
    "health": "/health"
  },
  "available_data": {
    "policies": 6,
    "procedures": 5,
    "contacts": 8
  }
}
```

### 2. **Health Check**

#### GET `/health`
Verifica el estado del servicio.

**Respuesta:**
```json
{
  "status": "healthy",
  "service": "corporate-api",
  "port": 8002
}
```

### 3. **Políticas Corporativas**

#### GET `/api/policies/{category}`
Obtiene información sobre una política específica.

**Parámetros:**
- `category` (string): Categoría de la política

**Categorías disponibles:**
- `vacaciones` - Política de vacaciones
- `teletrabajo` - Política de trabajo remoto
- `seguro_medico` - Beneficio de seguro médico
- `codigo_etica` - Código de ética empresarial
- `reembolsos` - Política de reembolso de gastos
- `horarios` - Política de horarios laborales

**Ejemplo de solicitud:**
```bash
curl http://localhost:8002/api/policies/vacaciones
```

**Respuesta exitosa (200):**
```json
{
  "success": true,
  "category": "vacaciones",
  "data": {
    "title": "Política de Vacaciones",
    "category": "Recursos Humanos",
    "effective_date": "2025-01-01",
    "description": "**Días disponibles:** 15 días hábiles al año..."
  }
}
```

**Respuesta de error (404):**
```json
{
  "detail": {
    "success": false,
    "message": "Política 'xxx' no encontrada",
    "available_categories": ["vacaciones", "teletrabajo", ...]
  }
}
```

### 4. **Procedimientos Administrativos**

#### GET `/api/procedures/{name}`
Obtiene los pasos de un procedimiento administrativo.

**Parámetros:**
- `name` (string): Nombre del procedimiento

**Procedimientos disponibles:**
- `solicitar_vacaciones` - Solicitud de vacaciones
- `reembolso_gastos` - Reembolso de gastos laborales
- `solicitar_equipo` - Solicitud de equipos de TI
- `cambio_datos_personales` - Actualización de datos personales
- `certificados_laborales` - Solicitud de certificados laborales

**Ejemplo de solicitud:**
```bash
curl http://localhost:8002/api/procedures/solicitar_vacaciones
```

**Respuesta exitosa (200):**
```json
{
  "success": true,
  "procedure": "solicitar_vacaciones",
  "data": {
    "name": "Solicitud de Vacaciones",
    "description": "Proceso para solicitar días de vacaciones...",
    "estimated_time": "3-5 días hábiles para aprobación",
    "requirements": "Mínimo 15 días de anticipación...",
    "steps": ["Paso 1: ...", "Paso 2: ...", ...],
    "important_notes": ["Nota 1", "Nota 2", ...]
  }
}
```

### 5. **Directorio de Contactos**

#### GET `/api/contacts/{department}`
Obtiene información de contacto de un departamento.

**Parámetros:**
- `department` (string): Nombre del departamento

**Departamentos disponibles:**
- `rrhh` - Recursos Humanos
- `ti` - Tecnología e Información
- `finanzas` - Departamento Financiero
- `legal` - Departamento Legal
- `marketing` - Marketing y Comunicaciones
- `operaciones` - Operaciones y Logística
- `capacitacion` - Capacitación y Desarrollo

**Ejemplo de solicitud:**
```bash
curl http://localhost:8002/api/contacts/rrhh
```

**Respuesta exitosa (200):**
```json
{
  "success": true,
  "department": "rrhh",
  "data": {
    "name": "Recursos Humanos",
    "department": "RRHH",
    "email": "rrhh@empresa.com",
    "phone": "+57 1 234-5678",
    "extension": "101",
    "location": "Edificio Central, Piso 3, Oficina 301",
    "hours": "Lunes a Viernes 8:00 AM - 5:00 PM",
    "manager": "María González",
    "services": ["Solicitud de vacaciones...", ...],
    "emergency_contact": "rrhh-urgencias@empresa.com"
  }
}
```

## 📝 Ejemplos de Uso

### Con cURL

```bash
# Obtener política de vacaciones
curl http://localhost:8002/api/policies/vacaciones

# Obtener procedimiento de reembolso
curl http://localhost:8002/api/procedures/reembolso_gastos

# Obtener contacto de TI
curl http://localhost:8002/api/contacts/ti
```

### Con Python (requests)

```python
import requests

# URL base de la API
BASE_URL = "http://localhost:8002"

# Consultar política de teletrabajo
response = requests.get(f"{BASE_URL}/api/policies/teletrabajo")
if response.status_code == 200:
    data = response.json()
    print(data["data"]["description"])

# Consultar contacto de RRHH
response = requests.get(f"{BASE_URL}/api/contacts/rrhh")
if response.status_code == 200:
    data = response.json()
    print(f"Email: {data['data']['email']}")
    print(f"Teléfono: {data['data']['phone']}")
```

### Con JavaScript (fetch)

```javascript
// Consultar procedimiento
fetch('http://localhost:8002/api/procedures/solicitar_equipo')
  .then(response => response.json())
  .then(data => {
    console.log(data.data.steps);
  });

// Consultar contacto
fetch('http://localhost:8002/api/contacts/finanzas')
  .then(response => response.json())
  .then(data => {
    console.log(`Email: ${data.data.email}`);
  });
```

## 🗂️ Estructura del Proyecto

```
corporate-api/
│
├── main.py                 # Aplicación principal de FastAPI
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Este archivo
│
└── data/                  # Archivos JSON con datos
    ├── contacts.json      # Directorio de contactos
    ├── policies.json      # Políticas corporativas
    └── procedures.json    # Procedimientos administrativos
```

## ⚙️ Configuración

### Puerto del Servidor
Por defecto, la API se ejecuta en el puerto **8002**. Para cambiar el puerto, modifica la línea en `main.py`:

```python
uvicorn.run(
    app,
    host="0.0.0.0",
    port=8002,  # Cambiar aquí
    log_level="info"
)
```

### CORS
La API tiene CORS habilitado para todas las origenes (`allow_origins=["*"]`). Para mayor seguridad en producción, especifica los dominios permitidos:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://tudominio.com"],
    ...
)
```

## 🛠️ Desarrollo

### Agregar Nuevas Políticas
Edita el archivo `data/policies.json`:

```json
{
  "nueva_politica": {
    "title": "Título de la Política",
    "category": "Categoría",
    "effective_date": "2025-01-01",
    "description": "Descripción detallada..."
  }
}
```

### Agregar Nuevos Procedimientos
Edita el archivo `data/procedures.json`:

```json
{
  "nuevo_procedimiento": {
    "name": "Nombre del Procedimiento",
    "description": "Descripción...",
    "estimated_time": "X días",
    "requirements": "Requisitos...",
    "steps": ["Paso 1", "Paso 2", ...],
    "important_notes": ["Nota 1", ...]
  }
}
```

### Agregar Nuevos Departamentos
Edita el archivo `data/contacts.json`:

```json
{
  "nuevo_depto": {
    "name": "Nombre del Departamento",
    "email": "email@empresa.com",
    "phone": "+57 1 234-5678",
    ...
  }
}
```

## 📊 Logs

La API registra todas las consultas y errores. Los logs incluyen:
- Consultas exitosas a endpoints
- Errores 404 (recursos no encontrados)
- Carga de datos al iniciar

Ejemplo de log:
```
2025-11-20 10:30:15 - INFO - Cargando datos corporativos...
2025-11-20 10:30:15 - INFO - ✓ 6 políticas cargadas
2025-11-20 10:30:15 - INFO - ✓ 5 procedimientos cargados
2025-11-20 10:30:15 - INFO - ✓ 8 contactos cargados
2025-11-20 10:30:15 - INFO - Corporate API lista en puerto 8002
2025-11-20 10:32:45 - INFO - Consultando política: vacaciones
```

## 🐛 Troubleshooting

### Error: Puerto 8002 ya está en uso
```powershell
# Encontrar el proceso usando el puerto
netstat -ano | findstr :8002

# Terminar el proceso (reemplaza PID con el número del proceso)
taskkill /PID <PID> /F
```

### Error: ModuleNotFoundError
```powershell
# Asegúrate de haber instalado las dependencias
pip install -r requirements.txt
```

### Error: Archivo JSON no encontrado
Verifica que la carpeta `data/` y los archivos JSON existan en la misma ubicación que `main.py`.

## 📄 Licencia

Este proyecto es un ejemplo educativo para demostración de APIs REST con FastAPI.

## 👥 Contacto

Para preguntas o sugerencias sobre esta API de demostración, contacta al equipo de desarrollo.

---

**Versión:** 1.0.0  
**Última actualización:** Noviembre 2025
