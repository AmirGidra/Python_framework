from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    navigationShopLink = (By.XPATH, "//a[@class='nav-link'][text()='Shop']")

    def shopItems(self):
        return self.driver.find_element(*HomePage.navigationShopLink)
