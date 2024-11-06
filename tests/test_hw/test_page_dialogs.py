from pages.base_page import BasePage
from pages.modal_dialogs import ModalDialogs
def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()

    assert modal_dialogs.btns_sub_menu.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()
    modal_dialogs.refresh()
    modal_dialogs.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert modal_dialogs.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)

