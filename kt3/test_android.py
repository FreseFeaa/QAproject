import pytest
from appium.webdriver.common.appiumby import AppiumBy
import time
@pytest.mark.parametrize("browser",["android"],indirect=True)
def test_android_browser(browser):
    el = browser.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Battery")')
    el.click()
    browser.save_screenshot("screen_battery.png")