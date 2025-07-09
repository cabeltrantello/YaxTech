from pydantic import BaseModel, Field
from typing import Dict, Any, Literal

#Using Literal for strict validation of HTTP methods.

HttpVerb = Literal["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"]

class MockResponseDefinition(BaseModel):
    status_code: int = Field(
        default=200,
        description="The HTTP status code to be returned for the mock.",
        example=200
    )
    headers: Dict[str, str] = Field(
        default_factory=dict,
        description="A dictionary of HTTP headers to be included in the response.",
        example={"X-Request-ID": "abc-123"}
    )
    body: Dict[str, Any] | list | None = Field(
        default=None,
        description="The JSON body of  the response.",
        example={"status": "operational", "healt_percentage": 100}
    )

class MockConfiguration(BaseModel):
    method: HttpVerb = Field(
        ...,
        description="The HTTP method match.",
        example="GET"
    )
    path: str = Field(
        ...,
        description="The request path to be simulated. It must start with a '/'.",
        pattern=r"^\/.*"
    )
    response: MockResponseDefinition = Field(
        ...,
        description="The response to be returned when the method and path match."
    )