from selenium.webdriver.common.by import By


class HomePage:

    navigationShopLink = (By.CSS_SELECTOR, "//a[@class='nav-link'][text()='Shop']")

    def __int__(self, driver):
        self.driver = driver

    def shopItems(self):
        return self.driver.find_element(HomePage.navigationShopLink)