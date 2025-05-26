import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser_setting():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
