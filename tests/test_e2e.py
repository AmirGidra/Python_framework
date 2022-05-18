from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        homepage = HomePage(self.driver)
        checkoutPage = homepage.shopItems()
        checkoutPage.selectProduct("Blackberry").click()
        checkoutPage.getCheckoutButton().click()
        confirmPage = checkoutPage.getCheckoutSuccessButton()
        confirmPage.getCountryField().send_keys("Sweden")
        confirmPage.selectDropdownCountry("Sweden").click()
        confirmPage.getTermCheckbox().click()
        confirmPage.getSubmitButton().click()
        successMessage = confirmPage.getSuccessMessage().text
        assert "Success!" in successMessage
