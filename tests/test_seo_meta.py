from pages.demoqa import DemoQa
from pages.accordian import Accordian
from pages.alert import Alerts
from pages.browser_tab import BrowserTab
import pytest
import time



@pytest.mark.parametrize('pages',[Accordian, Alerts, DemoQa, BrowserTab])
def test_check_titles_all_pages(browser,pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.viewport.exist()
    assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width,initial-scale=1'