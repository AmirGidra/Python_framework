from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitles = (By.CSS_SELECTOR, ".card-title a")
    addToCartButtons = (By.CSS_SELECTOR, ".card-footer button")
    checkoutButton = (By.CSS_SELECTOR, ".btn.btn-primary")
    checkoutSuccessButton = (By.CSS_SELECTOR, ".btn.btn-success")

    def getCardsTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitles)

    def getAddToCartButtons(self):
        return self.driver.find_elements(*CheckoutPage.addToCartButtons)

    def getCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)

    def getCheckoutSuccessButton(self):
        self.driver.find_element(*CheckoutPage.checkoutSuccessButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

    def selectProduct(self, product):
        titles = self.driver.find_elements(*CheckoutPage.cardTitles)
        i = -1
        for title in titles:
            i = i + 1
            if title.text == product:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                button = self.driver.find_elements(*CheckoutPage.addToCartButtons)
                return button[i]