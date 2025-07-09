from fastapi import APIRouter
from Backend.App.Api.v1.Endpoints import management, simulator

# This is the main router for the v1 API

api_v1_router = APIRouter()

api_v1_router.include_router(management.router, prefix="/_config", tags=["Management"])

api_v1_router.include_router(simulator.router, tags=["Simulator"])