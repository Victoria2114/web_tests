import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--start-maximized")
    # при желании: options.add_argument("--disable-dev-shm-usage"); options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)  # без Service/manager
    yield driver
    driver.quit()
