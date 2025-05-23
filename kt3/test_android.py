import pytest
from appium.webdriver.common.appiumby import AppiumBy

@pytest.mark.parametrize("browser",["android"],indirect=True)
def test_android_browser(browser):

    browser.get("https://ogorodnik.by/")
    browser.implicitly_wait(5)
    browser.find_elements(AppiumBy.CSS_SELECTOR,"[title='Поиск по каталогу']")[1].send_keys("Перец сладкий Аристотель F1")
    assert  browser.find_element(AppiumBy.CSS_SELECTOR,".stock.out-of-stock.wd-style-default").text == "Нет в наличии", "Под товаром НЕТ информации, что товвара нет!!!!"

    # browser.get("https://ogorodnik.by/")
    # # print(browser.page_source)
    # browser.find_element(AppiumBy.TAG_NAME, "TEXTAREA").send_keys("Meow")
    # browser.find_element(AppiumBy) 
    # el = browser.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Battery"))')
    # el.click()
    # print(browser.current_activity)
    # print(browser.current_context)
    # print(browser.current_package)
    # browser.activate_app("com.android.settings")
    # browser.save_screenshot("screen_battery.png")

