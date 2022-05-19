import pytest
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
import time


class TestHomePage(BaseClass):
    # Import data from fixture to test execution
    def test_populateLoginForm(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        confirmPage = ConfirmPage(self.driver)

        homePage.getName().send_keys(getData["firstName"])
        log.info("First name "+getData['firstName']+" entered successfully")
        homePage.getEmail().send_keys(getData["email"])
        log.info("Last name entered successfully")
        homePage.getpassword().send_keys("12345")
        log.info("Password entered successfully")
        self.selectDropdownValueByText(homePage.getGenderDropdown(), getData["gender"])
        homePage.getDate().send_keys("05/18/2022")
        confirmPage.getSubmitButton().click()
        log.info("Form submitted successfully")
        message = confirmPage.getSuccessMessage().text
        assert "Success" in message
        log.info("Success message displayed successfully")
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_Home_page_data)
    def getData(self, request):
        return request.param
