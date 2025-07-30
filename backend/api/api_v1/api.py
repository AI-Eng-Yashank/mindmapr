from fastapi import APIRouter, Depends

from api.api_v1.endpoints import mindmape_endpoint
from core.security import reusable_oauth2

api_router = APIRouter()

api_router.include_router(mindmape_endpoint.router, prefix="/mindmape", tags=["mindmaper"])

