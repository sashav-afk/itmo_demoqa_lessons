from pages.alert import Alerts
import time

def test_check_alert(browser):
    alert = Alerts(browser)
    alert.visit()

    alert.timerAlertButton.click()
    time.sleep(5)
    assert alert.alert().text == 'This alert appeared after 5 seconds'