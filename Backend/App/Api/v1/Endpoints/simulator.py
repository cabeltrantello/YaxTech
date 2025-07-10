from fastapi import APIRouter, Request, HTTPException, status
from fastapi.responses import JSONResponse
from Backend.App.Db.in_memory_db import mock_db
from Backend.App.Models.mock_request import DEFAULT_SCENARIO_NAME

router = APIRouter()

@router.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"])

async def catch_all_simulator(request: Request, full_path: str):
    path_with_leading_slash = f"/{full_path}"

    requested_scenario = request.query_params.get("scenario", DEFAULT_SCENARIO_NAME)

    found_mock = mock_db.find_mock(method=request.method, path=path_with_leading_slash)

    if not found_mock:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message": "No mock definition found for the requested path and method.",
                "requested_method": request.method,
                "requested_path": path_with_leading_slash
            }
        )
    
    response_def = found_mock.scenarios.get(requested_scenario, found_mock.scenarios[DEFAULT_SCENARIO_NAME])

    return JSONResponse(
        content=response_def.body,
        status_code=response_def.status_code,
        headers=response_def.headers
    )