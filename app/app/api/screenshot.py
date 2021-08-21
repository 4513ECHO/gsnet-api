import os

from fastapi import APIRouter
from fastapi.responses import FileResponse
from selenium import webdriver

def set_driver():
    _driver = webdriver.Remote(
        command_executor="http://selenium:4444/wd/hub",
    )
    return _driver

IMAGE_PATH = os.path.join(os.path.dirname(__file__), "image/screenshot.png")

router = APIRouter()

@router.get("/screenshot/{address}", response_class=FileResponse)
async def screenshot(address: str):
    driver = set_driver()
    driver.get(f"http://{address}/")
    screenshot = driver.save_screenshot(IMAGE_PATH)
    driver.quit()
    return FileResponse(screenshot)
