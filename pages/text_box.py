from pages.base_page import BasePage
from components.components import WebElement

class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.name = WebElement(driver,'#userName')
        self.address = WebElement(driver, '#currentAddress')
        self.submit = WebElement(driver, 'submit')
        self.element_1 = WebElement(driver, '#name.mb-1')
        self.element_2 = WebElement(driver, '#currentAddress.mb-1')
