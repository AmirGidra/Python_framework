from selenium.webdriver.support.select import Select

from Utilities.BaseClass import BaseClass
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
import time


class TestHomePage(BaseClass):

    def test_populateLoginForm(self):
        homePage = HomePage(self.driver)
        confirmPage = ConfirmPage(self.driver)

        homePage.getName().send_keys("Amir")
        homePage.getEmail().send_keys("a@test.com")
        homePage.getpassword().send_keys("12345")
        self.selectDropdownValueByText(homePage.getGenderDropdown(), "Female")
        homePage.getDate().send_keys("05/18/2022")
        confirmPage.getSubmitButton().click()
        message = confirmPage.getSuccessMessage().text
        print(message)
        assert "Success" in message
