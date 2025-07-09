from fastapi import APIRouter, Request, HTTPException, status
from fastapi.responses import JSONResponse
from Backend.App.Db.in_memory_db import mock_db