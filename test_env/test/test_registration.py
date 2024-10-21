from selenium import webdriver
import time
from selenium.webdriver.common.by import By

import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver

    driver.quit()

def test_registration(driver):
    driver.get("http://localhost:3000/")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,"#work-2").click()
     
    
