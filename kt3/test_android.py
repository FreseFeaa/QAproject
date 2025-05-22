import pytest
from appium.webdriver.common.appiumby import AppiumBy
import time
@pytest.mark.parametrize("browser",["android"],indirect=True)
def test_android_browser(browser):
    browser.find_element(AppiumBy) 



    # el = browser.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Battery"))')
    # el.click()
    # print(browser.current_activity)
    # print(browser.current_context)
    # print(browser.current_package)
    # browser.activate_app("com.android.settings")
    # browser.save_screenshot("screen_battery.png")

