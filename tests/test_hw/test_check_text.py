from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

# def test_check_text(browser):
#     demo_qa_page = DemoQa(browser)
#     demo_qa_page.visit()
#     assert demo_qa_page.text_folder.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
#
# def test_check_test_mid(browser):
#     demo_qa_page = DemoQa(browser)
#     elementsPage = ElementsPage(browser)
#     demo_qa_page.visit()
#     demo_qa_page.btn_elements.click()
#     assert elementsPage.text_mid.get_text() == 'Please select an item from left to start practice.'
#
# def test_page_elements(browser):
#     elementsPage = ElementsPage(browser)
#     elementsPage.visit()
#     assert elementsPage.text_elements.get_text() == 'Please select an item from left to start practice.'
#
# def test_page_browser(browser):
#     elementsPage = ElementsPage(browser)
#     elementsPage.visit()
#     assert  elementsPage.icon.exist()
#     assert elementsPage.btn_sidebar_first.exist()
#     assert elementsPage.btn_sidebar_first_textbox.exist()