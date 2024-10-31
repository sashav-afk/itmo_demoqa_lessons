from selenium.webdriver.common.by import By
from selenium.common import NoSuchFrameException

class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchFrameException:
            return False
        return True

    def get_text(self):
        str(self.find_element().text)