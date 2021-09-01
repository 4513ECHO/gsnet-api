import os
import datetime

from fastapi import APIRouter
from fastapi.responses import FileResponse, HTMLResponse, Response
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

router = APIRouter()
html = "<html><head><meta property='og:image' content='http://10.5.1.2:8000/api/screenshot?site={0}'></head></html>"


def create_image(url: str) -> str:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=options)
    driver.set_window_size(1200, 630)
    driver.get(url)
    filepath = f"/tmp/{datetime.datetime.now():%Y%m%d%H%M%S%f}.png"
    driver.save_screenshot(filepath)
    return filepath


def is_ipaddress(site: str) -> bool:
    if site.startswith("10."):
        return True
    return False


@router.get("/screenshot")
def screenshot(site: str, ogp: bool = False):
    if not is_ipaddress(site):
        return Response(status_code=400)
    if ogp:
        return HTMLResponse(html.format(site))
    else:
        image = create_image(f"http://{site}")
        return FileResponse(image)
