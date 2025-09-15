
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os

# Simple logger setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str):
        logging.info(f"Opening URL: {url}")
        self.driver.get(url)

    def find(self, locator):
        logging.info(f"Finding element: {locator}")
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except Exception as e:
            self._take_screenshot("find_error")
            logging.error(f"Element not found: {locator} | {e}")
            raise

    def click(self, locator):
        logging.info(f"Clicking element: {locator}")
        try:
            elem = self.wait.until(EC.element_to_be_clickable(locator))
            elem.click()
        except Exception as e:
            self._take_screenshot("click_error")
            logging.error(f"Failed to click element: {locator} | {e}")
            raise

    def type(self, locator, text: str):
        logging.info(f"Typing into element: {locator} -> '{text}'")
        try:
            elem = self.find(locator)
            elem.clear()
            elem.send_keys(text)
        except Exception as e:
            self._take_screenshot("type_error")
            logging.error(f"Failed to type into element: {locator} | {e}")
            raise

    def is_visible(self, locator) -> bool:
        logging.info(f"Checking visibility of element: {locator}")
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def _take_screenshot(self, reason: str):
        """Takes a screenshot on error with timestamp."""
        os.makedirs("screenshots", exist_ok=True)
        filename = f"screenshots/{reason}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        self.driver.save_screenshot(filename)
        logging.info(f"Saved screenshot: {filename}")
