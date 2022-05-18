from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    countyField = (By.ID, "country")
    termsCheckbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitButton = (By.XPATH, "//input[@type = 'submit']")
    successMessage = (By.CSS_SELECTOR, ".alert.alert-success")

    def getCountryField(self):
        return self.driver.find_element(*ConfirmPage.countyField)

    def selectDropdownCountry(self, country):
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, country)))
        return self.driver.find_element(By.LINK_TEXT, country)

    def getTermCheckbox(self):
        return self.driver.find_element(*ConfirmPage.termsCheckbox)

    def getSubmitButton(self):
        return self.driver.find_element(*ConfirmPage.submitButton)

    def getSuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.successMessage)
