from fastapi import APIRouter, status, Response
from Backend.App.Db.in_memory_db import mock_db
from Backend.App.Models.mock_request import MockConfiguration

router = APIRouter()

@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="REgister a Mock Configuration",
    description="Creates or updates a mock configuration. If a mock for the same method and path already exists, it will be overwritten.",
    response_description="The Mock configuration was succesfully registered"
)
async def register_mock_configuration(config: MockConfiguration):
    mock_db.add_mock(config)
    return Response(status_code=status.HTTP_201_CREATED)
