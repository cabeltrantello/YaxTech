from pydantic import BaseModel, Field, field_validator
from typing import Dict, Any, Literal
import base64

HttpVerb = Literal["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"]
DEFAULT_SCENARIO_NAME = "default"

class MockResponseDefinition(BaseModel):
    status_code: int = Field(default=200, example=200)
    headers: Dict[str, str] = Field(default_factory=dict, example={"X-Request-ID": "abc-123"})
    body: Dict[str, Any] | list | None = Field(default=None, example={"status": "operational"})

class MockDefinition(BaseModel):
    method: HttpVerb = Field(..., example="GET")
    path: str = Field(..., pattern=r"^\/.*", example="/api/v1/network-elements/bbu-4/status")
    
    scenarios: Dict[str, MockResponseDefinition] = Field(
        ...,
        description="A dictionary of response definitions, keyed by scenario name."
    )

    @field_validator('scenarios')
    @classmethod
    def must_contain_default_scenario(cls, v: Dict) -> Dict:
        if DEFAULT_SCENARIO_NAME not in v:
            raise ValueError("A 'default' scenario must be provided in the scenarios dictionary.")
        return v

    def generate_id(self) -> str:
        key = f"{self.method.upper()}:{self.path}"
        return base64.urlsafe_b64encode(key.encode()).decode()

class MockDefinitionWithId(MockDefinition):
    mock_id: str = Field(..., description="The unique, URL-safe identifier for the mock.", example="R0VUOjovYXBpL3YxL25ldHdvcmstZWxlbWVudHMvYmJ1LTQvc3RhdHVz")
