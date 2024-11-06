from components.components import WebElement
from pages.base_page import BasePage

class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_sub_menu = WebElement(driver, 'div:nth-child(1) > div > ul > li')
        self.icon = WebElement(driver, '#app > header > a')