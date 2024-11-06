import time

from pages.accordian import Accordian

def test_visible_accordion(browser):
    accor = Accordian(browser)
    accor.visit()
    assert accor.object.visible()
    accor.head.click()
    time.sleep(2)
    assert not accor.object.visible()

def test_visible_accordion_default(browser):
    accor = Accordian(browser)
    accor.visit()
    assert not accor.section2_1.visible()
    assert not accor.section2_2.visible()
    assert not accor.section3.visible()


