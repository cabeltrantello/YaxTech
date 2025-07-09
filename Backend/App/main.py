from fastapi import FastAPI
from Backend.App.Api.v1.api import api_v1_router

#Application metadata

app = FastAPI(
    title="YaxTech",
    description="A platform to simulate REST API endpoints of telecommunication network components for testing and development.",
    version="0.1.0",
    contact={
        "name": "Carlos Andrés Beltran Tello",
        "email": "cabeltrantello@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.include_router(api_v1_router, prefix="/api/v1")

@app.get("/", include_in_schema=False)
async def root():
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/docs")