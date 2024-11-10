from pages.base_page import BasePage
from components.components import WebElement

class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.first_name = WebElement(driver, '#fristName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.btn_submit = WebElement(driver, '#submit')
        self.btns_edit_record = WebElement(driver,'//*[@id="edit-record-1"]', 'xpath')
        self.btns_delite = WebElement(driver, '//*[@id="delete-record-1"]', 'xpath')
        self.heads_sort = WebElement(driver, '#div.rt-thead.-header > div > div:nth-child(1)')