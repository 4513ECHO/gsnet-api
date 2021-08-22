import os

from fastapi import APIRouter
from fastapi.responses import FileResponse
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class ExtDriver(webdriver.Remote):
    def __init__(self, url, image_path):
        super().__init__(
            desired_capabilities=DesiredCapabilities.FIREFOX.copy(),
            command_executor="http://0.0.0.0:4444/wd/hub",
        )
        self.url = url
        self.image_path = image_path

    def screenshot(self):
        super().get(self.url)
        return super().save_screenshot(self.image_path)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

IMAGE_PATH = os.path.join(os.path.dirname(__file__), "image/screenshot.png")

router = APIRouter()

@router.get("/screenshot/{address}", response_class=FileResponse)
async def screenshot(address: str):
    with ExtDriver(f"http://{address}/", IMAGE_PATH) as driver:
        screenshot = driver.screenshot()
    return FileResponse(screenshot)
