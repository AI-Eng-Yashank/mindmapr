from fastapi import APIRouter

from .endpoints import (
    mindmape_endpoint
)


route_v1 = APIRouter()

route_v1.include_router(mindmape_endpoint.router, prefix="/auth", tags=["auth"])