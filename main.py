"""
Corporate Information API
=========================

API REST que simula un sistema de información corporativa con:
- Políticas internas de la empresa
- Procedimientos administrativos
- Directorio de contactos

Puerto: 8002
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
from pathlib import Path
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Crear aplicación FastAPI
app = FastAPI(
    title="Corporate Information API",
    description="API de información corporativa para políticas, procedimientos y contactos",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directorio de datos
DATA_DIR = Path(__file__).parent / "data"

# Cargar datos al iniciar
def load_data(filename: str):
    """Carga datos desde archivo JSON"""
    try:
        file_path = DATA_DIR / filename
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"Archivo no encontrado: {filename}")
        return {}
    except json.JSONDecodeError as e:
        logger.error(f"Error al parsear JSON en {filename}: {e}")
        return {}

# Datos en memoria
POLICIES = {}
PROCEDURES = {}
CONTACTS = {}

@app.on_event("startup")
async def startup_event():
    """Cargar datos al iniciar la aplicación"""
    global POLICIES, PROCEDURES, CONTACTS
    
    logger.info("Cargando datos corporativos...")
    POLICIES = load_data("policies.json")
    PROCEDURES = load_data("procedures.json")
    CONTACTS = load_data("contacts.json")
    
    logger.info(f"✓ {len(POLICIES)} políticas cargadas")
    logger.info(f"✓ {len(PROCEDURES)} procedimientos cargados")
    logger.info(f"✓ {len(CONTACTS)} contactos cargados")
    logger.info("Corporate API lista en puerto 8002")

@app.get("/")
async def root():
    """Información sobre la API"""
    return {
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
            "policies": len(POLICIES),
            "procedures": len(PROCEDURES),
            "contacts": len(CONTACTS)
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "corporate-api",
        "port": 8002
    }

@app.get("/api/policies/{category}")
async def get_policy(category: str):
    """
    Obtiene información de una política específica.
    
    Args:
        category: Categoría de la política (vacaciones, teletrabajo, etc.)
    
    Returns:
        JSON con los detalles de la política
    """
    logger.info(f"Consultando política: {category}")
    
    category_key = category.lower().replace(" ", "_")
    
    if category_key in POLICIES:
        return {
            "success": True,
            "category": category,
            "data": POLICIES[category_key]
        }
    
    # Si no se encuentra, devolver error 404
    available = list(POLICIES.keys())
    logger.warning(f"Política no encontrada: {category}")
    raise HTTPException(
        status_code=404,
        detail={
            "success": False,
            "message": f"Política '{category}' no encontrada",
            "available_categories": available
        }
    )

@app.get("/api/procedures/{name}")
async def get_procedure(name: str):
    """
    Obtiene los pasos de un procedimiento administrativo.
    
    Args:
        name: Nombre del procedimiento (solicitar_vacaciones, reembolso_gastos, etc.)
    
    Returns:
        JSON con los pasos del procedimiento
    """
    logger.info(f"Consultando procedimiento: {name}")
    
    proc_key = name.lower().replace(" ", "_")
    
    if proc_key in PROCEDURES:
        return {
            "success": True,
            "procedure": name,
            "data": PROCEDURES[proc_key]
        }
    
    available = list(PROCEDURES.keys())
    logger.warning(f"Procedimiento no encontrado: {name}")
    raise HTTPException(
        status_code=404,
        detail={
            "success": False,
            "message": f"Procedimiento '{name}' no encontrado",
            "available_procedures": available
        }
    )

@app.get("/api/contacts/{department}")
async def get_contact(department: str):
    """
    Obtiene información de contacto de un departamento.
    
    Args:
        department: Nombre del departamento (rrhh, ti, finanzas, etc.)
    
    Returns:
        JSON con los datos de contacto
    """
    logger.info(f"Consultando contacto: {department}")
    
    dept_key = department.lower().replace(" ", "_")
    
    if dept_key in CONTACTS:
        return {
            "success": True,
            "department": department,
            "data": CONTACTS[dept_key]
        }
    
    available = list(CONTACTS.keys())
    logger.warning(f"Departamento no encontrado: {department}")
    raise HTTPException(
        status_code=404,
        detail={
            "success": False,
            "message": f"Departamento '{department}' no encontrado",
            "available_departments": available
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8002,
        log_level="info"
    )
