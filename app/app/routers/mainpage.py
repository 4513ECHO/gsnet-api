import os

from fastapi import (
    APIRouter,
    Request,
)
from fastapi.responses import HTMLResponse

router = APIRouter()

with open(os.path.join(os.path.dirname(__file__), "..", "static/index.html")) as f:
    html = f.read()


@router.get("/", response_class=HTMLResponse)
async def site_root(request: Request):
    return HTMLResponse(html)
