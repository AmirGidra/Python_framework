from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        homepage = HomePage(self.driver)
        homepage.shopItems().click()
        products = self.driver.find_elements(by=By.XPATH, value="//div[@class='card h-100']")
        for product in products:
            productName = product.find_element(by=By.XPATH, value="div/h4/a").text
            if productName == "Blackberry":
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                product.find_element(by=By.XPATH, value="div/button").click()

        self.driver.find_element(by=By.CSS_SELECTOR, value="a[class='nav-link btn btn-primary']").click()
        self.driver.find_element(by=By.XPATH, value="//button[@class = 'btn btn-success']").click()

        self.driver.find_element(by=By.ID, value="country").send_keys("India")