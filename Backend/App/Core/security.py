import os
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader

API_KEY_HEADER = APIKeyHeader(name="X-API-key")

MASTER_API_KEY = os.getenv("MASTER_API_KEY", "super-secret-dev-key")

async def get_api_key(api_key_header: str = Security(API_KEY_HEADER)):
    if api_key_header == MASTER_API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials. Invalid or missing API Key."
        )
    
