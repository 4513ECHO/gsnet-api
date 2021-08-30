import os

from fastapi import APIRouter
from fastapi.responses import FileResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

IMAGE_PATH = os.path.join(os.path.dirname(__file__), "image/screenshot.png")

router = APIRouter()

def create_driver(url, image_path):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(
        "/usr/lib/chromium-browser/chromedriver",
        options=options
    )
    driver.get(url)
    screenshot = driver.save_screenshot(image_path)

@router.get("/screenshot/{address}", response_class=FileResponse)
def screenshot(address: str):
    create_driver(f"http://{address}/", IMAGE_PATH)
    return FileResponse(IMAGE_PATH)
