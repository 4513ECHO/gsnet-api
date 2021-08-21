import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from .routers import mainpage
from .api import screenshot

STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")


def create_app():
    _app = FastAPI()

    _app.include_router(
        screenshot.router,
        prefix="/api",
        tags=["api"],
        responses={404: {"description": "not found"}},
    )

    _app.include_router(
        mainpage.router,
        prefix="/mainpage",
        tags=["mainpage"],
        responses={404: {"description": "not found"}},
    )

    _app.mount(
        "/static",
        StaticFiles(directory=STATIC_PATH, html=True),
        name="static"
    )

    return _app

app = create_app()

@app.get("/")
async def redirect_mainpage():
    return RedirectResponse("/mainpage")
