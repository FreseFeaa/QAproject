from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def reg_button_click(self):
        self.logger.info("Кликаем по кнопке регистрации")
        self.browser.find_element(*MainPageLocators.REG_BUTTON).click()
