import os
import datetime

from fastapi import APIRouter
from fastapi.responses import FileResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

router = APIRouter()

def create_image(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(
        "/usr/lib/chromium-browser/chromedriver",
        options=options
    )
    driver.get(url)
    image = f"{datetime.datetime.now():%Y%m%d%H%M%S%f}.png"
    driver.save_screenshot(f"/tmp/{image}")
    return image

@router.get("/screenshot/{address}", response_class=FileResponse)
def screenshot(address: str):
    image = create_image(f"http://{address}/")
    return FileResponse(f"/tmp/{image}")
