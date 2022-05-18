from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckoutPage


class HomePage:
    # Kreiramo constructor, preko kojeg cemo ubaciti webdriver pri samom inicijaliziranju objekta page klase
    def __init__(self, driver):
        self.driver = driver

    # TUPLE
    # element locators
    navigationShopLink = (By.XPATH, "//a[@class='nav-link'][text()='Shop']")
    # from fields
    nameField = (By.XPATH, "//form//input[@name='name']")
    emailField = (By.XPATH, "//form//input[@name='email']")
    passwordField = (By.ID, "exampleInputPassword1")
    genderDropdown = (By.TAG_NAME, "select")
    dateField = (By.CSS_SELECTOR, "input[name=bday]")

    # Moramo staviti zvijezdicu kada pozivamo TUPLE promjenjivu, da bi python mogao da je desijarilizira
    def shopItems(self):
        self.driver.find_element(*HomePage.navigationShopLink).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.nameField)

    def getEmail(self):
        return self.driver.find_element(*HomePage.emailField)

    def getpassword(self):
        return self.driver.find_element(*HomePage.passwordField)

    def getGenderDropdown(self):
        return self.driver.find_element(*HomePage.genderDropdown)

    def getDate(self):
        return self.driver.find_element(*HomePage.dateField)
