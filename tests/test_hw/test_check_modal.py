import time

from pages.modal_dialogs import ModalDialogs

def test_check_modal(browser):
    modal = ModalDialogs(browser)
    modal.visit()

    modal.small_modal.click()
    time.sleep(2)
    modal.close_small.click()
    modal.large_modal.click()
    time.sleep(2)
    modal.close_large.click()