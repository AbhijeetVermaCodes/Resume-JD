import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config import settings
from app.database import init_db
from app.api.routes import resume, job_description, analyze, config_routes, sample_data

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("resume_matcher")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize SQLite / PostgreSQL tables
    logger.info("Initializing database tables...")
    init_db()
    logger.info(f"{settings.app_name} v{settings.app_version} started successfully.")
    yield

# Also ensure DB tables initialized on import
init_db()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI-Powered Resume and Job Description Semantic Matcher & ATS Evaluator",
    lifespan=lifespan,
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount Routers
app.include_router(resume.router, prefix="/api")
app.include_router(job_description.router, prefix="/api")
app.include_router(analyze.router, prefix="/api")
app.include_router(config_routes.router, prefix="/api")
app.include_router(sample_data.router, prefix="/api")


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version,
        "llm_provider": settings.llm_provider,
        "gemini_enabled": bool(settings.gemini_api_key),
    }


# Global Exception Handler to avoid leaking internal stack traces
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error processing {request.method} {request.url.path}: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An internal error occurred while processing your request. Please check input formats and try again."}
    )
