from fastapi import APIRouter, status, Response, Depends, HTTPException
from typing import List
import base64
from Backend.App.Models.mock_request import MockDefinition, MockDefinitionWithId
from Backend.App.Db.in_memory_db import mock_db
from Backend.App.Core.security import get_api_key

router = APIRouter()
API_KEY_DEPENDENCY = Depends(get_api_key)

@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Register or Update a Mock Definition",
    response_model=MockDefinitionWithId
)
async def register_mock_definition(
    config: MockDefinition,
    api_key: str = API_KEY_DEPENDENCY
):
    mock_db.add_or_update_mock(config)
    return MockDefinitionWithId(**config.model_dump(), mock_id=config.generate_id())

@router.get(
    "",
    summary="List All Active Mock Definitions",
    response_model=List[MockDefinitionWithId]
)
async def list_all_mock_definitions(api_key: str = API_KEY_DEPENDENCY):
    all_mocks = mock_db.get_all_mocks()
    return [MockDefinitionWithId(**m.model_dump(), mock_id=m.generate_id()) for m in all_mocks]

def get_mock_from_id(mock_id: str) -> MockDefinition:
    try:
        decoded_key = base64.urlsafe_b64decode(mock_id).decode()
        method, path = decoded_key.split(":", 1)
        found_mock = mock_db.find_mock(method, path)
        if not found_mock:
            raise HTTPException(status_code=404, detail=f"Mock with ID '{mock_id}' not found.")
        return found_mock
    except (base64.binascii.Error, ValueError, IndexError):
        raise HTTPException(status_code=400, detail=f"Invalid mock ID format: '{mock_id}'.")

@router.get(
    "/{mock_id}",
    summary="Get a Specific Mock Definition by ID",
    response_model=MockDefinitionWithId
)
async def get_mock_definition_by_id(
    mock_id: str,
    api_key: str = API_KEY_DEPENDENCY
):
    found_mock = get_mock_from_id(mock_id)
    return MockDefinitionWithId(**found_mock.model_dump(), mock_id=found_mock.generate_id())

@router.put(
    "/{mock_id}",
    summary="Update a Specific Mock Definition by ID",
    response_model=MockDefinitionWithId
)
async def update_mock_definition_by_id(
    mock_id: str,
    config: MockDefinition,
    api_key: str = API_KEY_DEPENDENCY
):

    if mock_id != config.generate_id():
        raise HTTPException(
            status_code=409,
            detail="Mock ID in path does not match the mock definition in the request body."
        )
    
    mock_db.add_or_update_mock(config)
    return MockDefinitionWithId(**config.model_dump(), mock_id=config.generate_id())

@router.delete(
    "/{mock_id}",
    summary="Delete a Specific Mock Definition by ID",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_mock_definition_by_id(
    mock_id: str,
    api_key: str = API_KEY_DEPENDENCY
):
    found_mock = get_mock_from_id(mock_id) # First, ensure it exists
    deleted = mock_db.delete_mock(found_mock.method, found_mock.path)
    if not deleted:
        # This case should theoretically not be reached due to the check above
        raise HTTPException(status_code=500, detail="Failed to delete mock.")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
