from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture(scope="class")
def setUp(request):
    s = Service('Browser/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    url = 'https://rahulshettyacademy.com/angularpractice/'
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

