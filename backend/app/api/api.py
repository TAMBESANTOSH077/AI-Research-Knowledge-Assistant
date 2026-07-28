from fastapi import APIRouter

from app.api.routes.upload import router as upload_router
from app.api.routes.chat import router as chat_router
from app.api.routes.summary import router as summary_router

# New routes
from app.api.routes.analytics import router as analytics_router
from app.api.routes.search import router as search_router
from app.api.routes.files import router as files_router

api_router = APIRouter(prefix="/api")

# Existing routes
api_router.include_router(upload_router)
api_router.include_router(chat_router)
api_router.include_router(summary_router)

# New routes
api_router.include_router(files_router)
api_router.include_router(search_router)
api_router.include_router(analytics_router)

# Uncomment later when implemented
# from app.api.routes.history import router as history_router
# api_router.include_router(history_router)