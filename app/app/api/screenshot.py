import os

from fastapi import APIRouter
from fastapi.responses import FileResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

IMAGE_PATH = os.path.join(os.path.dirname(__file__), "image/screenshot.png")
CHROME_BIN = "/usr/bin/chromium-browser"
CHROME_DRIVER = "/usr/lib/chromium-browser/chromedriver"

router = APIRouter()

def create_driver(url, image_path):
    options = Options()
    options.binary_location = CHROME_BIN
    options.add_argument("--headless")
    driver = webdriver.Chrome(
        CHROME_DRIVER,
        options=Options,
    )
    driver.get(url)
    screenshot = driver.save_screenshot(image_path)
    return screenshot

@router.get("/screenshot/{address}", response_class=FileResponse)
def screenshot(address: str):
    screenshot = create_driver(f"http://{address}/", IMAGE_PATH)
    return FileResponse(screenshot)
