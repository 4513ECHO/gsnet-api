import os

from fastapi import APIRouter
from fastapi.responses import FileResponse
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

IMAGE_PATH = os.path.join(os.path.dirname(__file__), "image/screenshot.png")

router = APIRouter()

def create_driver(url, image_path):
    driver = webdriver.Remote(
        desired_capabilities=DesiredCapabilities.FIREFOX.copy(),
        command_executor="http://0.0.0.0:4444/wd/hub",
    )
    driver.get(url)
    screenshot = driver.save_screenshot(image_path)
    return screenshot

@router.get("/screenshot/{address}", response_class=FileResponse)
def screenshot(address: str):
    screenshot = create_driver(f"http://{address}/", IMAGE_PATH)
    return FileResponse(screenshot)
