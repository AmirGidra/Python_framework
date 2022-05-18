import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setUp")
class BaseClass:
    # Creating custom methods for explicit wait
    def verifyLinkPresence(self, textValue):
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, textValue)))

    def selectDropdownValueByText(self, locator, textValue):
        sel = Select(locator)
        sel.select_by_visible_text(textValue)
